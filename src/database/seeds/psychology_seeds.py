"""
知识库种子数据 - 心理健康标记
参照 ref.md 报告扩充
"""
from src.models.report import TraitCategory

PSYCHOLOGY_SEED_DATA = [
    # ============ 工作心态 ============
    {
        "rsid": "rs4680",
        "gene": "COMT",
        "category": TraitCategory.WORK_ATTITUDE,
        "clinical_significance": "Other",
        "phenotype": "抗压能力",
        "risk_allele": "A",
        "population_frequency": 0.50,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:12740595",
        "notes": "Met型(A)多巴胺清除慢，压力下可能易焦虑；Val型(G)清除快，抗压强但认知持久性稍弱",
        "trait_name": "抗压能力"
    },
    {
        "rsid": "rs53576",
        "gene": "OXTR",
        "category": TraitCategory.RELATIONSHIP,
        "clinical_significance": "Other",
        "phenotype": "共情能力",
        "risk_allele": "A",
        "population_frequency": 0.40,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:19641235",
        "notes": "AA/AG基因型可能在社交敏感度和共情方面略低，GG型通常共情能力更强",
        "trait_name": "共情能力"
    },
    {
        "rsid": "rs6265",
        "gene": "BDNF",
        "category": TraitCategory.PERSONALITY,
        "clinical_significance": "Other",
        "phenotype": "神经质倾向/焦虑",
        "risk_allele": "T",
        "population_frequency": 0.20,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:15654332",
        "notes": "Val66Met变异，Met(T)携带者可能更容易焦虑",
        "trait_name": "神经质倾向"
    },
    {
        "rsid": "rs1800497",
        "gene": "DRD2",
        "category": TraitCategory.WORK_ATTITUDE,
        "clinical_significance": "Other",
        "phenotype": "追求新奇倾向/成瘾易感性",
        "risk_allele": "T",
        "population_frequency": 0.33,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:1842353",
        "notes": "Taq1A A1等位基因(T)与多巴胺受体密度低相关，可能寻求刺激",
        "trait_name": "追求新奇倾向"
    },
    {
        "rsid": "rs6330",
        "gene": "SLC6A4",
        "category": TraitCategory.PERSONALITY,
        "clinical_significance": "Other",
        "phenotype": "乐观/悲观倾向",
        "risk_allele": "T",
        "population_frequency": 0.40,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:12444005",
        "notes": "5-HTTLPR (通过rs25531推断) 与情绪调节有关",
        "trait_name": "主观幸福感"
    },
    {
        "rsid": "rs17070145",
        "gene": "KIBRA",
        "category": TraitCategory.WORK_ATTITUDE,
        "clinical_significance": "Other",
        "phenotype": "情景记忆能力",
        "risk_allele": "T",
        "population_frequency": 0.25,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:17051233",
        "notes": "T等位基因与更好的情景记忆表现相关",
        "trait_name": "情景记忆能力"
    },
    {
        "rsid": "rs4343",
        "gene": "ACE",
        "category": TraitCategory.RELATIONSHIP,
        "clinical_significance": "Other",
        "phenotype": "社会信任水平",
        "risk_allele": "G",
        "population_frequency": 0.50,
        "evidence_level": "Low",
        "source": "Scientific Reports",
        "pmid": "PMID:28303893",
        "notes": "ACE基因变异可能通过催产素系统影响社会信任",
        "trait_name": "社会信任水平"
    }
]
