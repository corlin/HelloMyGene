
# 药物基因组学种子数据 (53种药物覆盖)
# 对应 ref.md 的用药指导

PGX_SEED_DATA = [
    # --- 抗炎和抗风湿 (CYP2C9) ---
    {
        "category": "抗炎和抗风湿药物", 
        "gene": "CYP2C9", 
        "rsid": "rs1057910", 
        "risk_allele": "C", 
        "notes": "影响布洛芬、塞来昔布、美洛昔康、氟比洛芬、氯诺昔康、吡罗昔康等代谢。*3等位基因导致代谢减慢，增加副作用风险。",
        "evidence_level": "1A"
    },
    
    # --- 抗肿瘤及免疫抑制剂 ---
    # TPMT (巯嘌呤、硫唑嘌呤、硫鸟嘌呤)
    {
        "category": "抗肿瘤及免疫抑制剂", 
        "gene": "TPMT", 
        "rsid": "rs1142345", 
        "risk_allele": "G", 
        "notes": "影响巯嘌呤、硫唑嘌呤、硫鸟嘌呤代谢。活性降低增加骨髓抑制风险。",
        "evidence_level": "1A"
    },
    # DPYD (卡培他滨、氟尿嘧啶、替加氟)
    {
        "category": "抗肿瘤及免疫抑制剂", 
        "gene": "DPYD", 
        "rsid": "rs3918290", 
        "risk_allele": "A", 
        "notes": "影响卡培他滨、氟尿嘧啶、替加氟代谢。缺陷者使用氟尿嘧啶类药物有致死风险。",
        "evidence_level": "1A"
    },
    # CYP3A5 (他克莫司)
    {
        "category": "抗肿瘤及免疫抑制剂", 
        "gene": "CYP3A5", 
        "rsid": "rs776746", 
        "risk_allele": "G", 
        "notes": "影响他克莫司代谢。*3/*3型代谢慢，需关注血药浓度。",
        "evidence_level": "1A"
    },

    # --- 抗感染药物 ---
    # NAT2 (异烟肼)
    {
        "category": "抗感染药物", 
        "gene": "NAT2", 
        "rsid": "rs1799930", 
        "risk_allele": "A", 
        "notes": "影响异烟肼代谢。慢的一酰化状态容易导致周围神经炎。",
        "evidence_level": "1A"
    },
    # CYP2C19 (伏立康唑)
    {
        "category": "抗感染药物", 
        "gene": "CYP2C19", 
        "rsid": "rs4244285", 
        "risk_allele": "A", 
        "notes": "影响伏立康唑代谢。慢代谢者浓度过高可能导致光毒性。",
        "evidence_level": "1A"
    },
    # IFNL3 (干扰素、利巴韦林)
    {
        "category": "抗感染药物", 
        "gene": "IFNL3", 
        "rsid": "rs12979860", 
        "risk_allele": "T", 
        "notes": "影响聚乙二醇干扰素治疗丙肝的疗效 (利巴韦林联合治疗)。CC型疗效好。",
        "evidence_level": "1A"
    },

    # --- 神经系统药物 (大部分 CYP2D6, CYP2C19) ---
    # CYP2D6 (可待因、曲马多、三环类、SSRIs)
    {
        "category": "神经系统药物", 
        "gene": "CYP2D6", 
        "rsid": "rs1065852", 
        "risk_allele": "A", 
        "notes": "影响可待因、曲马多(镇痛)、西酞普兰、帕罗西汀、文拉法辛、阿米替林(抗抑郁)、美托洛尔(心血管)等多种药物。",
        "evidence_level": "1A"
    },
    
    # --- 消化系统药物 (CYP2C19) ---
    # 已经在抗感染中覆盖了 CYP2C19，但为了分类清晰，还是在 reporter 中处理映射。
    # 这里添加另一个 CYP2C19 位点作为补充，或者复用。
    # 为了种子数据完整性，我们可以添加 CYP2C19*3
    {
        "category": "消化系统药物",
        "gene": "CYP2C19",
        "rsid": "rs4986893",
        "risk_allele": "A",
        "notes": "影响奥美拉唑、兰索拉唑等PPI类药物代谢。慢代谢者抑酸效果更好。",
        "evidence_level": "1A"
    },

    # --- 心血管系统药物 ---
    # SLCO1B1 (他汀类)
    {
        "category": "心血管系统药物", 
        "gene": "SLCO1B1", 
        "rsid": "rs4149056", 
        "risk_allele": "C", 
        "notes": "影响辛伐他汀、阿托伐他汀、瑞舒伐他汀转运。CC型发生肌病风险显著增加。",
        "evidence_level": "1A"
    },
    # VKORC1 (华法林)
    {
        "category": "心血管系统药物", 
        "gene": "VKORC1", 
        "rsid": "rs9923231", 
        "risk_allele": "T", 
        "notes": "影响华法林剂量敏感性。AA型敏感，需低剂量。",
        "evidence_level": "1A"
    },
    # CYP2C9 (华法林、苯妥英) - 已在抗炎中覆盖，但苯妥英属神经。
    
    # 其他药物
    # clopidogrel (CYP2C19)
    # Siponimod (CYP2C9)
]
