"""
数据库初始化
创建知识库表并加载种子数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

from src.models.variant import Base, VariantAnnotation
from src.database.seeds import ALL_SEED_DATA


DATABASE_PATH = Path(__file__).parent.parent.parent / "data" / "knowledge_base" / "variants.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


def get_engine():
    """获取数据库引擎"""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(DATABASE_URL, echo=False)


def get_session():
    """获取数据库会话"""
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def init_database(force_recreate: bool = False):
    """初始化数据库并加载种子数据"""
    engine = get_engine()
    
    if force_recreate and DATABASE_PATH.exists():
        DATABASE_PATH.unlink()
    
    # 创建表
    Base.metadata.create_all(engine)
    
    # 加载种子数据
    session = get_session()
    
    try:
        existing_count = session.query(VariantAnnotation).count()
        if existing_count > 0:
            print(f"数据库已有 {existing_count} 条记录，跳过种子数据加载")
            return existing_count
        
        for data in ALL_SEED_DATA:
            variant = VariantAnnotation(**data)
            session.merge(variant)  # 使用merge避免重复
        
        session.commit()
        count = session.query(VariantAnnotation).count()
        print(f"成功加载 {count} 条种子数据到知识库")
        return count
        
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def query_variant(rsid: str) -> VariantAnnotation | None:
    """查询单个变异"""
    session = get_session()
    try:
        return session.query(VariantAnnotation).filter_by(rsid=rsid).first()
    finally:
        session.close()


def query_variants_by_category(category: str) -> list[VariantAnnotation]:
    """按类别查询变异"""
    session = get_session()
    try:
        return session.query(VariantAnnotation).filter_by(category=category).all()
    finally:
        session.close()


if __name__ == "__main__":
    init_database(force_recreate=True)
