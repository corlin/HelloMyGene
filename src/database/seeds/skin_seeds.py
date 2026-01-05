"""
知识库种子数据 - 皮肤特征标记
参照 ref.md 报告扩充
"""
from src.models.report import TraitCategory

SKIN_SEED_DATA = [
    # ============ 抗晒/美白 ============
    {
        "rsid": "rs1805007",
        "gene": "MC1R",
        "category": TraitCategory.WHITENING,
        "clinical_significance": "Other",
        "phenotype": "抗晒黑能力/红发",
        "risk_allele": "T",
        "population_frequency": 0.10,
        "evidence_level": "High",
        "source": "GWAS",
        "pmid": "PMID:10729795",
        "notes": "Arg151Cys，T纯合子皮肤白皙，抗晒能力弱，易晒伤不易晒黑",
        "trait_name": "抗晒黑能力"
    },
    {
        "rsid": "rs1800566",
        "gene": "NQO1",
        "category": TraitCategory.ANTI_AGING,
        "clinical_significance": "Other",
        "phenotype": "皮肤抗氧化能力",
        "risk_allele": "T",
        "population_frequency": 0.20,
        "evidence_level": "High",
        "source": "Journal",
        "pmid": "PMID:18431804",
        "notes": "酶活性降低，抗氧化能力减弱，需加强外部抗氧化",
        "trait_name": "皮肤抗氧化能力"
    },
    {
        "rsid": "rs12203592",
        "gene": "IRF4",
        "category": TraitCategory.SPOTS,
        "clinical_significance": "Other",
        "phenotype": "雀斑易感性",
        "risk_allele": "T",
        "population_frequency": 0.15,
        "evidence_level": "GWAS Catalog",
        "source": "GWAS",
        "pmid": "PMID:18488028",
        "notes": "与皮肤色素沉着斑点（雀斑）相关",
        "trait_name": "雀斑"
    },
    {
        "rsid": "rs3825942",
        "gene": "LOXL1",
        "category": TraitCategory.SKIN_PROBLEM,
        "clinical_significance": "Other",
        "phenotype": "皮肤松弛/弹性",
        "risk_allele": "G",
        "population_frequency": 0.50,
        "evidence_level": "GWAS",
        "source": "GWAS",
        "pmid": "PMID:17690259",
        "notes": "与弹性纤维形成有关，影响皮肤松弛风险",
        "trait_name": "眼皮松弛"
    },
    {
        "rsid": "rs3219155",
        "gene": "AGER",
        "category": TraitCategory.ANTI_AGING,
        "clinical_significance": "Other",
        "phenotype": "抗糖化能力",
        "risk_allele": "T",
        "population_frequency": 0.30,
        "evidence_level": "Medium",
        "source": "Study",
        "pmid": "PMID:20531818",
        "notes": "晚期糖基化终末产物受体基因，变异可能影响糖化反应",
        "trait_name": "抗糖化能力"
    }
]
