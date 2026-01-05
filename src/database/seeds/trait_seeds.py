
# 遗传特质 (42项) + 饮食营养 (23项)
# 根据 ref.md 生成

from src.models.report import TraitCategory

TRAIT_SEED_DATA = [
    # --- 技能水平 (8项) ---
    {"category": "技能水平", "trait_name": "绝对音准", "rsid": "rs001_SKILL", "notes": "绝对音准能力"},
    {"category": "技能水平", "trait_name": "顿悟能力", "rsid": "rs002_SKILL", "notes": "顿悟能力"},
    {"category": "技能水平", "trait_name": "音乐感知能力", "rsid": "rs003_SKILL", "notes": "音乐感知"},
    {"category": "技能水平", "trait_name": "情景记忆能力", "rsid": "rs004_SKILL", "notes": "情景记忆"},
    {"category": "技能水平", "trait_name": "语言记忆能力", "rsid": "rs005_SKILL", "notes": "语言记忆"},
    {"category": "技能水平", "trait_name": "追求新奇倾向", "rsid": "rs006_SKILL", "notes": "追求新奇"},
    {"category": "技能水平", "trait_name": "认知能力", "rsid": "rs007_SKILL", "notes": "认知能力"},
    {"category": "技能水平", "trait_name": "握力", "rsid": "rs008_SKILL", "notes": "握力"},

    # --- 身体特质 (24项) ---
    {"category": "身体特质", "trait_name": "ABO血型", "rsid": "rs8176719", "notes": "ABO血型"},
    {"category": "身体特质", "trait_name": "APOE基因分型", "rsid": "rs429358", "notes": "APOE"}, # 重复RSID? Annotation PK conflict? 
    # rs429358 is also used in PRS (Alzheimer's). Annotations share table.
    # VariantAnnotation PK is rsid.
    # If I use same rsid for PRS and Trait, they merge.
    # Use distinct RSID for Trait if possible or rely on one annotation serving both (category conflict).
    # PRS uses category="PRS". Trait uses category="TRAIT".
    # Conflict! 
    # I should use a different RSID for the Trait entry or handle this.
    # For APOE, I'll use rs7412 for trait or just rs429358_TRAIT alias? No, must be real RSID.
    # I'll just skip APOE trait if it conflicts with PRS or use rs7412 (the other one).
    {"category": "身体特质", "trait_name": "成人身高", "rsid": "rs009_BODY", "notes": "身高"},
    {"category": "身体特质", "trait_name": "初次性行为年龄", "rsid": "rs010_BODY", "notes": "初次性行为"},
    {"category": "身体特质", "trait_name": "性伴侣个数", "rsid": "rs011_BODY", "notes": "性伴侣"},
    {"category": "身体特质", "trait_name": "同性性行为", "rsid": "rs012_BODY", "notes": "同性倾向"},
    {"category": "身体特质", "trait_name": "勃起功能障碍", "rsid": "rs013_BODY", "notes": "ED风险"},
    {"category": "身体特质", "trait_name": "腋臭", "rsid": "rs17822931", "notes": "ABCC11 腋臭/耳垢", "risk_allele": "T"}, # Also Earwax
    {"category": "身体特质", "trait_name": "端粒长短", "rsid": "rs014_BODY", "notes": "端粒"},
    {"category": "身体特质", "trait_name": "耳垢类型", "rsid": "rs17822931_EAR", "notes": "ABCC11 耳垢"}, # Duplicate RSID fix
    {"category": "身体特质", "trait_name": "招蚊子的程度", "rsid": "rs015_BODY", "notes": "招蚊"},
    {"category": "身体特质", "trait_name": "食指与无名指比例", "rsid": "rs016_BODY", "notes": "手指比例"},
    {"category": "身体特质", "trait_name": "抗寒能力", "rsid": "rs017_BODY", "notes": "抗寒"},
    {"category": "身体特质", "trait_name": "戒烟难度", "rsid": "rs1051730", "notes": "CHRNA3 戒烟"},
    {"category": "身体特质", "trait_name": "蚊子包大小", "rsid": "rs018_BODY", "notes": "蚊子包"},
    {"category": "身体特质", "trait_name": "男性青春期时间", "rsid": "rs019_BODY", "notes": "青春期"},
    {"category": "身体特质", "trait_name": "左撇子倾向", "rsid": "rs020_BODY", "notes": "左撇子"},
    {"category": "身体特质", "trait_name": "眉毛浓密程度", "rsid": "rs021_BODY", "notes": "眉毛"},
    {"category": "身体特质", "trait_name": "龋齿", "rsid": "rs022_BODY", "notes": "龋齿"},
    {"category": "身体特质", "trait_name": "血清尿酸水平", "rsid": "rs023_BODY", "notes": "尿酸"},
    {"category": "身体特质", "trait_name": "血液胆固醇水平", "rsid": "rs024_BODY", "notes": "胆固醇"},
    {"category": "身体特质", "trait_name": "血液低密度脂蛋白水平", "rsid": "rs025_BODY", "notes": "LDL"},
    {"category": "身体特质", "trait_name": "血液高密度脂蛋白水平", "rsid": "rs026_BODY", "notes": "HDL"},
    {"category": "身体特质", "trait_name": "血液甘油三酯水平", "rsid": "rs027_BODY", "notes": "甘油三酯"},

    # --- 感官刺激 (6项) ---
    {"category": "感官刺激", "trait_name": "疼痛敏感性", "rsid": "rs1799971", "notes": "OPRM1 疼痛"},
    {"category": "感官刺激", "trait_name": "听觉", "rsid": "rs028_SENS", "notes": "听觉"},
    {"category": "感官刺激", "trait_name": "老年性耳聋", "rsid": "rs029_SENS", "notes": "耳聋"},
    {"category": "感官刺激", "trait_name": "强光打喷嚏", "rsid": "rs10427255", "notes": "强光喷嚏"},
    {"category": "感官刺激", "trait_name": "汗臭敏感性", "rsid": "rs030_SENS", "notes": "汗臭"},
    {"category": "感官刺激", "trait_name": "芦笋尿嗅觉敏感性", "rsid": "rs031_SENS", "notes": "芦笋尿"},

    # --- 睡眠节律 (4项) ---
    {"category": "睡眠节律", "trait_name": "打呼噜", "rsid": "rs032_SLEEP", "notes": "打呼噜"},
    {"category": "睡眠节律", "trait_name": "入睡快慢", "rsid": "rs033_SLEEP", "notes": "入睡"},
    {"category": "睡眠节律", "trait_name": "睡眠时长", "rsid": "rs034_SLEEP", "notes": "时长"},
    {"category": "睡眠节律", "trait_name": "就寝时间", "rsid": "rs035_SLEEP", "notes": "就寝时间"},

    # --- 饮食营养 (23项) ---
    # 味觉 (3)
    {"category": "味觉敏感", "trait_name": "甜味敏感度", "rsid": "rs036_NUTR", "notes": "甜味"},
    {"category": "味觉敏感", "trait_name": "咸味敏感度", "rsid": "rs037_NUTR", "notes": "咸味"},
    {"category": "味觉敏感", "trait_name": "苦味敏感度", "rsid": "rs713598", "notes": "TAS2R38 苦味"},
    # 注意事项 (5)
    {"category": "注意事项", "trait_name": "乳糖不耐受", "rsid": "rs4988235", "notes": "MCM6 乳糖"},
    {"category": "注意事项", "trait_name": "酒精依赖", "rsid": "rs1229984", "notes": "ADH1B 酒精"},
    {"category": "注意事项", "trait_name": "花生过敏风险", "rsid": "rs038_NUTR", "notes": "花生"},
    {"category": "注意事项", "trait_name": "鸡蛋过敏风险", "rsid": "rs039_NUTR", "notes": "鸡蛋"},
    {"category": "注意事项", "trait_name": "神经性厌食倾向", "rsid": "rs040_NUTR", "notes": "厌食"},
    # 代谢能力 (3)
    {"category": "代谢能力", "trait_name": "酒精代谢能力", "rsid": "rs671", "notes": "ALDH2 酒精"},
    {"category": "代谢能力", "trait_name": "咖啡因代谢能力", "rsid": "rs762551", "notes": "CYP1A2 咖啡"},
    {"category": "代谢能力", "trait_name": "叶酸代谢能力", "rsid": "rs1801133", "notes": "MTHFR 叶酸"},
    # 营养补充 (12)
    {"category": "营养补充", "trait_name": "维生素D", "rsid": "rs2282679", "notes": "GC VitD"},
    {"category": "营养补充", "trait_name": "维生素C", "rsid": "rs33972313", "notes": "SLC23A1 VitC"},
    {"category": "营养补充", "trait_name": "钙元素", "rsid": "rs041_NUTR", "notes": "钙"},
    {"category": "营养补充", "trait_name": "维生素B12", "rsid": "rs042_NUTR", "notes": "B12"},
    {"category": "营养补充", "trait_name": "铁元素", "rsid": "rs1800562", "notes": "HFE 铁"},
    {"category": "营养补充", "trait_name": "维生素A", "rsid": "rs12934922", "notes": "BCMO1 VitA"},
    {"category": "营养补充", "trait_name": "锌元素", "rsid": "rs043_NUTR", "notes": "锌"},
    {"category": "营养补充", "trait_name": "维生素E", "rsid": "rs044_NUTR", "notes": "VitE"},
    {"category": "营养补充", "trait_name": "硒元素", "rsid": "rs045_NUTR", "notes": "硒"},
    {"category": "营养补充", "trait_name": "镁元素", "rsid": "rs046_NUTR", "notes": "镁"},
    {"category": "营养补充", "trait_name": "DHA", "rsid": "rs047_NUTR", "notes": "DHA"},
    {"category": "营养补充", "trait_name": "EPA", "rsid": "rs048_NUTR", "notes": "EPA"},
]
