"""
变异注释数据模型
定义知识库中的变异分类信息
"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer, Enum as SQLEnum
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class VariantCategory(str, Enum):
    """变异分类类型"""
    ACMG = "ACMG"           # ACMG 临床可报告变异
    PGX = "PGX"             # 药物基因组学
    PRS = "PRS"             # 多基因风险评分标记
    TRAIT = "TRAIT"         # 性状相关
    

class ClinicalSignificance(str, Enum):
    """临床意义分级"""
    PATHOGENIC = "Pathogenic"
    LIKELY_PATHOGENIC = "Likely Pathogenic"
    VUS = "Uncertain Significance"
    LIKELY_BENIGN = "Likely Benign"
    BENIGN = "Benign"
    RISK_FACTOR = "Risk Factor"


class VariantAnnotation(Base):
    """变异注释数据库模型"""
    __tablename__ = "variants"
    
    rsid = Column(String(20), primary_key=True, index=True)
    gene = Column(String(50), nullable=True, index=True)
    category = Column(String(20), nullable=False)
    clinical_significance = Column(String(50), nullable=True)
    phenotype = Column(String(500), nullable=True)
    risk_allele = Column(String(10), nullable=True)
    population_frequency = Column(Float, nullable=True)
    evidence_level = Column(String(20), nullable=True)
    source = Column(String(50), nullable=True)
    pmid = Column(String(100), nullable=True)
    notes = Column(String(1000), nullable=True)
    prevention = Column(String(1000), nullable=True)
    suggested_tests = Column(String(500), nullable=True)
    trait_name = Column(String(100), nullable=True)


class VariantAnnotationSchema(BaseModel):
    """变异注释 Pydantic Schema (用于API)"""
    rsid: str
    gene: Optional[str] = None
    category: VariantCategory
    clinical_significance: Optional[str] = None
    phenotype: Optional[str] = None
    risk_allele: Optional[str] = None
    population_frequency: Optional[float] = None
    evidence_level: Optional[str] = None
    source: Optional[str] = None
    pmid: Optional[str] = None
    notes: Optional[str] = None
    
    class Config:
        from_attributes = True
