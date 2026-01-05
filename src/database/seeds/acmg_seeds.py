"""
知识库种子数据 - ACMG 临床可报告变异
基于 ACMG SF v3.2 的部分关键 SNP
"""

ACMG_SEED_DATA = [
    # BRCA1/BRCA2 - 遗传性乳腺/卵巢癌
    {
        "rsid": "rs80357906",
        "gene": "BRCA1",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "遗传性乳腺/卵巢癌综合征",
        "risk_allele": "T",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:25741868",
        "notes": "5382insC 移码突变，高度致病性"
    },
    {
        "rsid": "rs80359550",
        "gene": "BRCA2",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "遗传性乳腺/卵巢癌综合征",
        "risk_allele": "A",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:25741868",
        "notes": "6174delT 移码突变"
    },
    
    # LDLR - 家族性高胆固醇血症
    {
        "rsid": "rs28942078",
        "gene": "LDLR",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "家族性高胆固醇血症",
        "risk_allele": "T",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:30239722",
        "notes": "导致LDL受体功能缺失"
    },
    
    # KCNQ1 - 长QT综合征
    {
        "rsid": "rs199472709",
        "gene": "KCNQ1",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "长QT综合征1型 (LQT1)",
        "risk_allele": "A",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:20301448",
        "notes": "心律失常风险，需避免剧烈运动和某些药物"
    },
    
    # MLH1 - Lynch综合征
    {
        "rsid": "rs63750447",
        "gene": "MLH1",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "Lynch综合征 (遗传性非息肉性结直肠癌)",
        "risk_allele": "A",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:24362816",
        "notes": "结直肠癌和子宫内膜癌风险显著增加"
    },
    
    # TP53 - Li-Fraumeni综合征
    {
        "rsid": "rs28934578",
        "gene": "TP53",
        "category": "ACMG",
        "clinical_significance": "Pathogenic",
        "phenotype": "Li-Fraumeni综合征",
        "risk_allele": "A",
        "evidence_level": "ACMG SF v3.2",
        "source": "ClinVar",
        "pmid": "PMID:20301488",
        "notes": "多种肿瘤高风险，需终生监测"
    },
]
