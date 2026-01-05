"""
知识库种子数据 - 运动健康标记
参照 ref.md 报告扩充
"""
from src.models.report import TraitCategory

SPORTS_SEED_DATA = [
    # ============ 身体素质 ============
    {
        "rsid": "rs1815739",
        "gene": "ACTN3",
        "category": TraitCategory.ENDURANCE,
        "clinical_significance": "Other",
        "phenotype": "爆发力 vs 耐力",
        "risk_allele": "T",
        "population_frequency": 0.40,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:12879365",
        "notes": "R577X变异，XX型(TT)快肌纤维缺乏，更适合耐力运动；RR型适合爆发力",
        "trait_name": "爆发力"
    },
    {
        "rsid": "rs4253778",
        "gene": "PPARA",
        "category": TraitCategory.ENDURANCE,
        "clinical_significance": "Other",
        "phenotype": "耐力表现",
        "risk_allele": "C",
        "population_frequency": 0.20,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:15672079",
        "notes": "G等位基因与更好的耐力表现相关，C可能较弱",
        "trait_name": "耐力"
    },
    {
        "rsid": "rs9939609",
        "gene": "FTO",
        "category": TraitCategory.WEIGHT_LOSS,
        "clinical_significance": "Other",
        "phenotype": "肥胖风险/减肥效果",
        "risk_allele": "A",
        "population_frequency": 0.30,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:17434869",
        "notes": "肥胖易感基因，运动对携带者的减肥效果尤为显著",
        "trait_name": "运动减肥效果"
    },
    
    # ============ 受伤风险 ============
    {
        "rsid": "rs679620",
        "gene": "MMP3",
        "category": TraitCategory.INJURY_RISK,
        "clinical_significance": "Other",
        "phenotype": "跟腱炎风险",
        "risk_allele": "G",
        "population_frequency": 0.45,
        "evidence_level": "Medium",
        "source": "Study",
        "pmid": "PMID:18949660",
        "notes": "GG基因型可能增加跟腱病变风险，需注意热身",
        "trait_name": "跟腱损伤"
    },
    {
        "rsid": "rs12722",
        "gene": "COL5A1",
        "category": TraitCategory.INJURY_RISK,
        "clinical_significance": "Other",
        "phenotype": "软组织损伤风险",
        "risk_allele": "T",
        "population_frequency": 0.55,
        "evidence_level": "Medium",
        "source": "Study",
        "pmid": "PMID:20556780",
        "notes": "胶原蛋白基因，影响肌腱灵活性和受伤风险，T型可能增加风险",
        "trait_name": "韧带损伤"
    },
    {
        "rsid": "rs1800795",
        "gene": "IL6",
        "category": TraitCategory.EXERCISE_EFFECT,
        "clinical_significance": "Other",
        "phenotype": "运动后恢复/炎症反应",
        "risk_allele": "C",
        "population_frequency": 0.25,
        "evidence_level": "Medium",
        "source": "Study",
        "pmid": "PMID:16518765",
        "notes": "G174C，C等位基因可能导致恢复期炎症水平较低，恢复较快",
        "trait_name": "运动后恢复速度"
    }
]
