"""
基因型数据解析器
解析原始基因芯片数据文件（TSV格式）
"""
from typing import Generator
from pathlib import Path
import pandas as pd
from pydantic import BaseModel


class GenotypeRecord(BaseModel):
    """单个基因型记录"""
    rsid: str           # SNP ID, e.g., "rs369986014"
    chromosome: str     # 染色体, e.g., "1", "X", "MT"
    position: int       # 染色体位置
    genotype: str       # 基因型, e.g., "GG", "AG", "--", "ID"
    
    @property
    def is_valid(self) -> bool:
        """检查是否为有效基因型（非缺失）"""
        return self.genotype not in ("--", "")
    
    @property
    def alleles(self) -> tuple[str, str] | None:
        """返回等位基因对，如 ("A", "G")"""
        if not self.is_valid or len(self.genotype) != 2:
            return None
        return (self.genotype[0], self.genotype[1])


class GenotypeParser:
    """基因型文件解析器"""
    
    EXPECTED_COLUMNS = ["gxid", "chromosome", "position", "genotype"]
    
    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"基因型文件不存在: {filepath}")
    
    def parse(self) -> Generator[GenotypeRecord, None, None]:
        """逐行解析基因型文件，返回生成器"""
        with open(self.filepath, 'r') as f:
            header = f.readline().strip().split('\t')
            
            # 验证列名
            if header != self.EXPECTED_COLUMNS:
                raise ValueError(f"文件格式错误，期望列: {self.EXPECTED_COLUMNS}, 实际: {header}")
            
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) != 4:
                    continue
                
                rsid, chrom, pos, geno = parts
                
                # 跳过重复的 rsid (如 rs2710890.2)
                if '.' in rsid.split('rs')[-1]:
                    continue
                
                yield GenotypeRecord(
                    rsid=rsid,
                    chromosome=chrom,
                    position=int(pos),
                    genotype=geno
                )
    
    def to_dataframe(self) -> pd.DataFrame:
        """将数据加载为 Pandas DataFrame"""
        records = list(self.parse())
        return pd.DataFrame([r.model_dump() for r in records])
    
    def count_records(self) -> int:
        """统计有效记录数"""
        return sum(1 for _ in self.parse())
    
    def get_stats(self) -> dict:
        """获取文件统计信息"""
        df = self.to_dataframe()
        valid_count = df[df['genotype'] != '--'].shape[0]
        missing_count = df[df['genotype'] == '--'].shape[0]
        
        # 染色体排序函数
        def chrom_sort_key(x):
            if x.isdigit():
                return (0, int(x))
            elif x == 'X':
                return (1, 0)
            elif x == 'Y':
                return (1, 1)
            elif x == 'MT':
                return (1, 2)
            else:
                return (2, 0)
        
        return {
            "total_records": len(df),
            "valid_genotypes": valid_count,
            "missing_genotypes": missing_count,
            "missing_rate": round(missing_count / len(df) * 100, 2) if len(df) > 0 else 0,
            "chromosomes": sorted(df['chromosome'].unique().tolist(), key=chrom_sort_key)
        }
