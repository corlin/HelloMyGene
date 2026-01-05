"""
变异注释器
将用户的基因型数据与知识库进行匹配
"""
from typing import Generator
from src.analysis.parser import GenotypeRecord
from src.database.init_db import get_session
from src.models.variant import VariantAnnotation


class AnnotatedVariant:
    """注释后的变异结果"""
    def __init__(self, genotype: GenotypeRecord, annotation: VariantAnnotation | None):
        self.genotype = genotype
        self.annotation = annotation
    
    @property
    def is_annotated(self) -> bool:
        return self.annotation is not None
    
    @property
    def has_risk_allele(self) -> bool:
        """检查用户是否携带风险等位基因"""
        if not self.annotation or not self.annotation.risk_allele:
            return False
        if not self.genotype.alleles:
            return False
        return self.annotation.risk_allele in self.genotype.alleles
    
    @property
    def risk_allele_count(self) -> int:
        """计算风险等位基因拷贝数 (0, 1, 2)"""
        if not self.annotation or not self.annotation.risk_allele:
            return 0
        if not self.genotype.alleles:
            return 0
        return self.genotype.alleles.count(self.annotation.risk_allele)
    
    def to_dict(self) -> dict:
        """转换为字典"""
        result = {
            "rsid": self.genotype.rsid,
            "chromosome": self.genotype.chromosome,
            "position": self.genotype.position,
            "genotype": self.genotype.genotype,
            "is_annotated": self.is_annotated,
        }
        
        if self.annotation:
            result.update({
                "gene": self.annotation.gene,
                "category": self.annotation.category,
                "clinical_significance": self.annotation.clinical_significance,
                "phenotype": self.annotation.phenotype,
                "risk_allele": self.annotation.risk_allele,
                "has_risk_allele": self.has_risk_allele,
                "risk_allele_count": self.risk_allele_count,
                "evidence_level": self.annotation.evidence_level,
                "notes": self.annotation.notes,
            })
        
        return result


class VariantAnnotator:
    """变异注释引擎"""
    
    def __init__(self):
        self._cache: dict[str, VariantAnnotation | None] = {}
        self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """加载知识库到内存缓存"""
        session = get_session()
        try:
            variants = session.query(VariantAnnotation).all()
            for v in variants:
                self._cache[v.rsid] = v
        finally:
            session.close()
    
    def annotate(self, genotype: GenotypeRecord) -> AnnotatedVariant:
        """注释单个基因型"""
        annotation = self._cache.get(genotype.rsid)
        return AnnotatedVariant(genotype, annotation)
    
    def annotate_batch(self, genotypes: list[GenotypeRecord]) -> list[AnnotatedVariant]:
        """批量注释"""
        return [self.annotate(g) for g in genotypes]
    
    def find_significant(self, genotypes: list[GenotypeRecord]) -> list[AnnotatedVariant]:
        """找出有临床意义的变异"""
        results = []
        for g in genotypes:
            annotated = self.annotate(g)
            if annotated.is_annotated and annotated.has_risk_allele:
                results.append(annotated)
        return results
    
    def group_by_category(self, annotated_variants: list[AnnotatedVariant]) -> dict[str, list[AnnotatedVariant]]:
        """按类别分组"""
        groups = {}
        for av in annotated_variants:
            if av.annotation:
                cat = av.annotation.category
                if cat not in groups:
                    groups[cat] = []
                groups[cat].append(av)
        return groups
