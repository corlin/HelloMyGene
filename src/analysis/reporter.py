"""
报告生成器
将注释结果生成结构化报告
"""
from datetime import datetime
from uuid import uuid4
from typing import Optional

from src.analysis.parser import GenotypeParser, GenotypeRecord
from src.analysis.annotator import VariantAnnotator, AnnotatedVariant
from src.models.report import (
    GeneReport, ACMGFinding, PGxResult, PRSResult, TraitResult,
    RiskLevel, DrugResponse, AlertItem, DrugCategory, TraitCategory
)


class ReportGenerator:
    """报告生成器"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.parser = GenotypeParser(filepath)
        self.annotator = VariantAnnotator()
    
    def generate(self) -> GeneReport:
        """生成完整报告"""
        # 解析基因型数据
        genotypes = list(self.parser.parse())
        stats = self.parser.get_stats()
        
        # 注释变异
        significant = self.annotator.find_significant(genotypes)
        grouped = self.annotator.group_by_category(significant)
        
        # 收集各分类变异
        all_pgx_vars = []
        all_trait_vars = []
        all_prs_vars = grouped.get("PRS", [])
        
        # 遍历所有分组，归类到 PGX 或 TRAIT
        for cat, vars in grouped.items():
            if cat == "PGX" or cat in [e.value for e in DrugCategory]:
                all_pgx_vars.extend(vars)
            elif cat == "TRAIT" or cat in [e.value for e in TraitCategory]:
                all_trait_vars.extend(vars)
            elif cat == "PRS":
                pass # 已经在上面获取
        
        # 生成各模块结果
        acmg_findings = self._process_acmg(grouped.get("ACMG", []))
        pgx_results = self._process_pgx(all_pgx_vars)
        prs_results = self._process_prs(all_prs_vars)
        trait_results = self._process_traits(all_trait_vars)
        
        # 生成需注意项
        alert_items = self._generate_alert_items(prs_results, pgx_results, trait_results)
        
        return GeneReport(
            report_id=str(uuid4())[:8],
            generated_at=datetime.now(),
            sample_id=self.filepath.split("/")[-1].replace(".txt", ""),
            # 模拟个人信息
            user_name="张三",
            gender="男",
            age=30,
            sample_type="唾液",
            
            total_variants=stats["total_records"],
            valid_variants=stats["valid_genotypes"],
            missing_rate=stats["missing_rate"],
            acmg_findings=acmg_findings,
            pgx_results=pgx_results,
            prs_results=prs_results,
            trait_results=trait_results,
            alert_items=alert_items
        )
    
    def _process_acmg(self, variants: list[AnnotatedVariant]) -> list[ACMGFinding]:
        """处理 ACMG 临床变异"""
        results = []
        for av in variants:
            if av.annotation:
                results.append(ACMGFinding(
                    rsid=av.genotype.rsid,
                    gene=av.annotation.gene or "Unknown",
                    phenotype=av.annotation.phenotype or "",
                    clinical_significance=av.annotation.clinical_significance or "",
                    recommendation=av.annotation.notes,
                    pmid=av.annotation.pmid,
                ))
        return results
    
    def _process_pgx(self, variants: list[AnnotatedVariant]) -> list[PGxResult]:
        """处理药物基因组学变异"""
        results = []
        # 去重：一个RSID可能对应多个药物分类（虽然现在种子是从分类来的，但为了安全）
        seen_rsids = set()
        
        for av in variants:
            rsid = av.genotype.rsid
            if rsid in seen_rsids:
                continue
            seen_rsids.add(rsid)
            
            if av.annotation:
                # 根据基因型判断代谢表型
                phenotype = self._determine_metabolizer_status(av)
                
                # 确定分类
                category = DrugCategory.OTHER
                if av.annotation.category in [e.value for e in DrugCategory]:
                    category = DrugCategory(av.annotation.category)
                
                # 判断是否需要注意
                needs_attention = phenotype != DrugResponse.NORMAL_METABOLIZER
                
                results.append(PGxResult(
                    gene=av.annotation.gene or "Unknown",
                    rsid=rsid,
                    genotype=av.genotype.genotype,
                    phenotype=phenotype,
                    category=category,  # 新增字段
                    needs_attention=needs_attention, # 新增字段
                    affected_drugs=self._get_affected_drugs(av.annotation.gene),
                    recommendation=av.annotation.notes or "",
                    evidence_level=av.annotation.evidence_level,
                ))
        return results
    
    def _process_prs(self, variants: list[AnnotatedVariant]) -> list[PRSResult]:
        """处理多基因风险评分 - 基于优势比的风险计算"""
        import math
        
        # 疾病相关位点的优势比 (OR) 配置 (部分示例，未配置的使用默认值)
        OR_CONFIG = {
            "rs1801133": {"disease": "冠心病", "or": 1.2, "raf": 0.3}, 
            "rs429358": {"disease": "阿尔茨海默病", "or": 3.68, "raf": 0.15},
            "rs7412": {"disease": "阿尔茨海默病", "or": 0.62, "raf": 0.08},
            "rs356219": {"disease": "帕金森病", "or": 1.35, "raf": 0.40},
        }
        
        # 按疾病分组
        disease_variants = {}
        for av in variants:
            # 提取疾病名称
            # 优先使用 annotation 中的 phenotype，或者根据 category/source 判断
            # 如果是 PRS 类别的，annotation.phenotype 应该包含疾病名
            disease_name = self._extract_disease(av.annotation.phenotype or "")
            if not disease_name: 
                continue
                
            group = av.annotation.source or "Disease"
            
            if disease_name not in disease_variants:
                disease_variants[disease_name] = {
                    "variants": [],
                    "prevention": av.annotation.prevention,
                    "suggested_tests": av.annotation.suggested_tests,
                    "group": group
                }
            
            # 确定参数
            rsid = av.genotype.rsid
            if rsid in OR_CONFIG:
                or_val = OR_CONFIG[rsid]["or"]
                raf = OR_CONFIG[rsid]["raf"]
            else:
                # 默认参数
                or_val = 1.3
                raf = 0.2
                
            disease_variants[disease_name]["variants"].append({
                "av": av,
                "or": or_val,
                "raf": raf
            })
        
        results = []
        for disease, data in disease_variants.items():
            var_list = data["variants"]
            group = data["group"]
            
            # 计算累积风险分数
            log_or_sum = 0.0
            for v in var_list:
                allele_count = v["av"].risk_allele_count
                effect_or = v["or"]
                if effect_or > 0:
                    log_or_sum += math.log(effect_or) * allele_count
            
            relative_risk = math.exp(log_or_sum)
            z_score = log_or_sum / 0.5
            percentile = self._norm_cdf(z_score) * 100
            
            # 风险等级
            if percentile >= 80:
                risk_level = RiskLevel.HIGH
            elif percentile >= 60:
                risk_level = RiskLevel.MODERATE
            elif percentile >= 40:
                risk_level = RiskLevel.LOW
            else:
                risk_level = RiskLevel.NORMAL
            
            # 解读
            interpretation = f"您的{disease}遗传风险打分为{relative_risk:.2f} (人群平均1.0)。"
            if risk_level == RiskLevel.HIGH:
                interpretation += " 属于高风险人群。"
            elif risk_level == RiskLevel.MODERATE:
                interpretation += " 属于中等风险人群。"
            else:
                interpretation += " 风险处于一般水平。"
            
            results.append(PRSResult(
                disease=disease,
                score=round(relative_risk, 2),
                percentile=round(percentile, 1),
                risk_level=risk_level,
                population_average=1.0,
                interpretation=interpretation,
                prevention=data["prevention"],
                suggested_tests=data["suggested_tests"],
                group=group
            ))
        
        return results
    
    def _norm_cdf(self, z: float) -> float:
        """标准正态分布累积分布函数 (近似)"""
        import math
        # 使用误差函数近似
        return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
    
    def _process_traits(self, variants: list[AnnotatedVariant]) -> list[TraitResult]:
        """处理性状分析"""
        results = []
        # 去重
        seen_rsids = set()
        
        for av in variants:
            rsid = av.genotype.rsid
            if rsid in seen_rsids:
                continue
            seen_rsids.add(rsid)
            
            if av.annotation:
                result_text = self._interpret_trait(av)
                
                # 确定分类
                category = TraitCategory.OTHER
                if av.annotation.category in [e.value for e in TraitCategory]:
                    category = TraitCategory(av.annotation.category)
                else: 
                     # 尝试从硬编码映射中获取（兼容旧逻辑）
                     pass
                
                results.append(TraitResult(
                    trait_name=av.annotation.trait_name or self._extract_trait_name(av.annotation.phenotype or ""),
                    category=category,
                    rsid=rsid,
                    genotype=av.genotype.genotype,
                    result=result_text,
                    description=av.annotation.notes or "",
                ))
        return results

    def _generate_alert_items(self, prs_results: list[PRSResult], pgx_results: list[PGxResult], trait_results: list[TraitResult]) -> list[AlertItem]:
        """生成需注意项目与建议"""
        alerts = []
        
        # 1. 高风险疾病 (PRS)
        for prs in prs_results:
            if prs.risk_level == RiskLevel.HIGH:
                alerts.append(AlertItem(
                    item_name=prs.disease,
                    result="高风险",
                    prevention=prs.prevention,
                    suggested_tests=prs.suggested_tests,
                    priority=1
                ))
        
        # 2. 药物风险 (PGx)
        for pgx in pgx_results:
            if pgx.needs_attention:
                alerts.append(AlertItem(
                    item_name=f"{pgx.gene}相关药物",
                    result=pgx.phenotype.value if hasattr(pgx.phenotype, 'value') else str(pgx.phenotype),
                    prevention=f"建议咨询医生调整用药方案。{pgx.recommendation}",
                    suggested_tests="相关药物代谢酶检测",
                    priority=2
                ))

        # 3. 特定严重性状 (Traits) - 示例
        for trait in trait_results:
            if "缺乏" in trait.result or "风险增加" in trait.result or "敏感性高" in trait.result:
                # 筛选一些重要的
                if trait.category in [TraitCategory.VITAMIN, TraitCategory.METABOLISM, TraitCategory.ALLERGY]:
                     alerts.append(AlertItem(
                        item_name=trait.trait_name,
                        result=trait.result,
                        prevention=trait.description,
                        suggested_tests="相关生化指标检测",
                        priority=3
                    ))
        
        # 排序：优先级高的在前
        alerts.sort(key=lambda x: x.priority)
        return alerts
    
    def _determine_metabolizer_status(self, av: AnnotatedVariant) -> DrugResponse:
        """根据基因型判断代谢状态"""
        count = av.risk_allele_count
        if count == 2:
            return DrugResponse.POOR_METABOLIZER
        elif count == 1:
            return DrugResponse.INTERMEDIATE_METABOLIZER
        else:
            return DrugResponse.NORMAL_METABOLIZER
    
    def _get_affected_drugs(self, gene: Optional[str]) -> list[str]:
        """获取受影响的药物列表 (扩展版)"""
        if not gene: return []
        drug_map = {
            "CYP2C19": ["氯吡格雷", "奥美拉唑", "兰索拉唑", "泮托拉唑", "艾司奥美拉唑", "伏立康唑", "西酞普兰", "艾司西酞普兰", "舍曲林", "地西泮", "信必可"],
            "CYP2D6": ["可待因", "曲马多", "文拉法辛", "帕罗西汀", "美托洛尔", "比索洛尔", "卡维地洛", "阿米替林", "多塞平", "丙咪嗪", "阿立哌唑", "利培酮", "氯氮平", "奥氮平", "氟伏沙明", "苯妥英"],
            "CYP2C9": ["布洛芬", "塞来昔布", "美洛昔康", "氟比洛芬", "氯诺昔康", "吡罗昔康", "华法林", "西尼莫德", "苯妥英"],
            "SLCO1B1": ["辛伐他汀", "阿托伐他汀", "瑞舒伐他汀", "普伐他汀", "匹伐他汀"],
            "VKORC1": ["华法林"],
            "TPMT": ["巯嘌呤", "硫唑嘌呤", "硫鸟嘌呤"],
            "NUDT15": ["巯嘌呤", "硫唑嘌呤", "硫鸟嘌呤"],
            "DPYD": ["卡培他滨", "氟尿嘧啶", "替加氟"],
            "NAT2": ["异烟肼"],
            "IFNL3": ["聚乙二醇干扰素α-2a", "聚乙二醇干扰素α-2b", "利巴韦林"],
            "CYP3A5": ["他克莫司"],
            "G6PD": ["磺胺类", "阿司匹林(大剂量)"],
            "HLA-B": ["卡马西平", "奥卡西平", "别嘌醇", "阿巴卡韦"],
            "ABCB1": ["地高辛"]
        }
        return drug_map.get(gene, [])
    
    def _extract_disease(self, phenotype: str) -> str:
        """从表型描述提取疾病名称"""
        if "冠心病" in phenotype:
            return "冠心病"
        if "冠心病" in phenotype:
            return "冠心病"
        elif "胰腺癌" in phenotype:
            return "胰腺癌风险"
        elif "近视" in phenotype:
            return "近视风险"
        elif "硬皮病" in phenotype:
            return "硬皮病风险"
        elif "糖尿病" in phenotype:
            return "2型糖尿病"
        elif "阿尔茨海默" in phenotype:
            return "阿尔茨海默病"
        return phenotype.split("(")[0].strip()
    
    def _extract_trait_name(self, phenotype: str) -> str:
        """提取性状名称"""
        return phenotype.split("(")[0].strip()
    
    def _interpret_trait(self, av: AnnotatedVariant) -> str:
        """解读性状结果 - 详细版"""
        count = av.risk_allele_count
        gene = av.annotation.gene if av.annotation else ""
        rsid = av.genotype.rsid
        genotype = av.genotype.genotype
        
        # 详细的性状解读配置
        TRAIT_INTERPRETATIONS = {
            # 叶酸代谢
            "rs1801133": {
                2: "叶酸代谢能力显著降低(TT型)，建议补充活性叶酸(5-MTHF)",
                1: "叶酸代谢能力轻度降低(CT型)，建议适量补充叶酸",
                0: "叶酸代谢能力正常(CC型)"
            },
            "rs1801131": {
                2: "A1298C纯合变异，与C677T复合可进一步影响叶酸代谢",
                1: "A1298C杂合，单独影响较小",
                0: "A1298C位点正常"
            },
            # 咖啡因
            "rs762551": {
                2: "咖啡因慢代谢型(CC)，建议减少咖啡摄入",
                1: "咖啡因中间代谢型(AC)",
                0: "咖啡因快代谢型(AA)，可适量饮用咖啡"
            },
            # 乳糖
            "rs4988235": {
                2: "乳糖耐受型(AA)，成年后可正常消化乳制品",
                1: "乳糖部分耐受(AG)",
                0: "乳糖不耐受型(GG)，建议选择无乳糖产品"
            },
            # 酒精代谢
            "rs671": {
                2: "ALDH2完全缺乏(AA)，饮酒后严重面红，应避免饮酒",
                1: "ALDH2活性降低(AG)，饮酒后面红，建议少量饮酒",
                0: "ALDH2活性正常(GG)，酒精代谢能力正常"
            },
            "rs1229984": {
                2: "酒精快速代谢型(AA)，酒精依赖风险较低",
                1: "酒精代谢中间型(AG)",
                0: "酒精正常代谢型(GG)"
            },
            # 眼睛颜色
            "rs12913832": {
                2: "棕色眼睛概率高(AA)",
                1: "眼睛颜色中间型(AG)",
                0: "蓝色眼睛概率>99%(GG)"
            },
            # 耳垢
            "rs17822931": {
                2: "干性耳垢(TT)，东亚人常见类型",
                1: "耳垢类型中间(CT)",
                0: "湿性耳垢(CC)，欧洲人常见类型"
            },
            # 运动能力
            "rs1815739": {
                2: "耐力型肌肉(TT)，适合长跑等有氧运动",
                1: "混合型肌肉(CT)",
                0: "爆发力型肌肉(CC)，适合短跑、举重等"
            },
            # 脂肪代谢
            "rs4994": {
                2: "脂肪燃烧效率降低(AA)，需要更多运动控制体重",
                1: "脂肪代谢中间型(AG)",
                0: "脂肪燃烧效率正常(GG)"
            },
            # 维生素D
            "rs2282679": {
                2: "维生素D水平偏低风险(CC)，建议适当补充",
                1: "维生素D水平中间型(AC)",
                0: "维生素D水平正常倾向(AA)"
            },
            # 苦味感知
            "rs713598": {
                2: "苦味敏感型(CC/PAV)，可能不喜欢西兰花等蔬菜",
                1: "苦味中间敏感型",
                0: "苦味不敏感型(GG/AVI)"
            },
            # 睡眠节律
            "rs1801260": {
                2: "夜猫子型(CC)，倾向晚睡晚起",
                1: "睡眠习惯中间型",
                0: "早起型(TT)"
            },
            # 阳光喷嚏
            "rs10427255": {
                2: "阳光喷嚏反射明显(CC)，看到阳光容易打喷嚏",
                1: "阳光喷嚏反射中等(CT)",
                0: "无阳光喷嚏反射(TT)"
            },
            # 香菜
            "rs72921001": {
                2: "香菜味觉异常(AA)，闻到香菜有肥皂味",
                1: "香菜味觉部分异常(CA)",
                0: "香菜味觉正常(CC)"
            },
            # 皮肤
            "rs1805007": {
                2: "晒伤敏感性高(TT)，皮肤癌风险增加",
                1: "晒伤敏感性中等(CT)",
                0: "晒伤敏感性正常(CC)"
            },
            # β-胡萝卜素
            "rs12934922": {
                2: "β-胡萝卜素转化能力降低50%(TT)，建议直接补充维生素A",
                1: "β-胡萝卜素转化能力轻度降低",
                0: "β-胡萝卜素转化能力正常"
            },
        }
        
        # 查找特定位点的解读
        if rsid in TRAIT_INTERPRETATIONS:
            interpretations = TRAIT_INTERPRETATIONS[rsid]
            return interpretations.get(count, interpretations.get(1, "携带相关等位基因"))
        
        # 通用解读
        if count >= 2:
            return "纯合携带相关等位基因"
        elif count == 1:
            return "杂合携带相关等位基因"
        return "未携带相关等位基因"
