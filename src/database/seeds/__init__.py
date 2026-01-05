# 种子数据导出
from .acmg_seeds import ACMG_SEED_DATA
from .pgx_seeds import PGX_SEED_DATA
from .prs_seeds import PRS_SEED_DATA
from .trait_seeds import TRAIT_SEED_DATA
from .ancestry_seeds import ANCESTRY_SEED_DATA
from .psychology_seeds import PSYCHOLOGY_SEED_DATA
from .skin_seeds import SKIN_SEED_DATA
from .sports_seeds import SPORTS_SEED_DATA

ALL_SEED_DATA = (
    ACMG_SEED_DATA + 
    PGX_SEED_DATA + 
    PRS_SEED_DATA + 
    TRAIT_SEED_DATA +
    ANCESTRY_SEED_DATA +
    PSYCHOLOGY_SEED_DATA +
    SKIN_SEED_DATA +
    SPORTS_SEED_DATA
)
