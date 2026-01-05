"""
报告数据模型
定义分析报告的结构 - 基于 ref.md 专业报告格式
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class RiskLevel(str, Enum):
    """风险等级"""
    HIGH = "高风险"
    MODERATE = "中等风险"
    LOW = "低风险"
    NORMAL = "正常"
    UNKNOWN = "未知"


class DrugResponse(str, Enum):
    """药物代谢表型"""
    POOR_METABOLIZER = "慢代谢型"
    INTERMEDIATE_METABOLIZER = "中间代谢型"
    NORMAL_METABOLIZER = "正常代谢型"
    RAPID_METABOLIZER = "快代谢型"
    ULTRA_RAPID_METABOLIZER = "超快代谢型"


class DrugCategory(str, Enum):
    """药物类别 - 参照ref.md"""
    ANTI_INFLAMMATORY = "抗炎和抗风湿药物"
    ANTITUMOR = "抗肿瘤及免疫抑制剂"
    ANTI_INFECTIVE = "抗感染药物"
    NERVOUS_SYSTEM = "神经系统药物"
    DIGESTIVE_SYSTEM = "消化系统药物"
    CARDIOVASCULAR = "心血管系统药物"
    OTHER = "其他药物"


class TraitCategory(str, Enum):
    """性状类别 - 扩展版"""
    # 遗传特质
    SKILL = "技能水平"
    BODY = "身体特质"
    SENSORY = "感官刺激"
    SLEEP = "睡眠节律"
    # 饮食营养
    TASTE = "味觉敏感"
    ALLERGY = "注意事项"
    METABOLISM = "代谢能力"
    NUTRITION = "营养补充"
    # 皮肤特征
    ANTI_AGING = "抗衰"
    WHITENING = "美白"
    SPOTS = "色斑"
    SKIN_QUALITY = "肤质"
    SKIN_PROBLEM = "皮肤问题"
    # 运动健康
    BODY_CONSTITUTION = "基础体质"
    ENDURANCE = "耐力&爆发力"
    INJURY_RISK = "受伤风险"
    WEIGHT_LOSS = "减肥必看"
    EXERCISE_EFFECT = "效果提升"
    # 心理健康
    WORK_ATTITUDE = "工作心态"
    RELATIONSHIP = "人际关系"
    PERSONALITY = "性格特点"
    # 其他
    ALCOHOL = "酒精代谢"
    APPEARANCE = "外貌特征"
    VITAMIN = "维生素代谢"
    OTHER = "其他特征"


class AlertItem(BaseModel):
    """需注意项目 - 参照ref.md第117-134行"""
    item_name: str  # 需注意事项
    result: str  # 基因检测结果
    prevention: Optional[str] = None  # 预防建议
    suggested_tests: Optional[str] = None  # 建议检查项目
    priority: int = 0  # 优先级(用于排序)


class ACMGFinding(BaseModel):
    """ACMG 临床发现"""
    rsid: str
    gene: str
    phenotype: str
    clinical_significance: str
    inheritance: Optional[str] = None
    recommendation: Optional[str] = None
    pmid: Optional[str] = None


class PGxResult(BaseModel):
    """药物基因组学结果"""
    gene: str
    rsid: str
    genotype: str
    phenotype: DrugResponse
    category: DrugCategory = DrugCategory.OTHER
    affected_drugs: list[str]
    recommendation: str
    evidence_level: Optional[str] = None
    needs_attention: bool = False  # 需关注用药风险


class PRSResult(BaseModel):
    """多基因风险评分结果"""
    disease: str
    score: float
    percentile: float
    risk_level: RiskLevel
    population_average: float
    interpretation: str
    prevention: Optional[str] = None  # 预防建议
    suggested_tests: Optional[str] = None  # 建议检查项目
    group: str = "Disease" # 分组: Disease / Tumor


class TraitResult(BaseModel):
    """性状分析结果"""
    trait_name: str
    category: TraitCategory = TraitCategory.OTHER
    rsid: str
    genotype: str
    result: str
    description: str


class GeneReport(BaseModel):
    """完整基因报告 - 专业版"""
    report_id: str
    generated_at: datetime
    sample_id: str
    
    # 个人信息
    user_name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    sample_type: str = "口腔拭子"
    
    # 摘要统计
    total_variants: int
    valid_variants: int
    missing_rate: float
    
    # 需注意项目
    alert_items: list[AlertItem] = []
    
    # 分析结果
    acmg_findings: list[ACMGFinding] = []
    pgx_results: list[PGxResult] = []
    prs_results: list[PRSResult] = []
    trait_results: list[TraitResult] = []
    
    # 元数据
    analysis_version: str = "2.0.0"
    disclaimer: str = "本报告仅供参考，不构成医疗建议。检测结果只能解释基因层面的部分因素，后天环境、生活方式等非遗传因素也会影响实际表现。请咨询专业医生获取个性化指导。"

