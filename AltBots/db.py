"""
Persistent sudo storage via Supabase (asyncpg).
Same project as Swastika, different table prefix: Swastika_
"""

import logging
from os import getenv
from typing import List, Optional, Set

import asyncpg

log = logging.getLogger("db")

_pool: Optional[asyncpg.Pool] = None

DB_HOST = getenv("DB_HOST", "")
DB_PORT = int(getenv("DB_PORT", "5432"))
DB_USER = getenv("DB_USER", "")
DB_PASSWORD = getenv("DB_PASSWORD", "")
DB_NAME = getenv("DB_NAME", "postgres")
TABLE_PREFIX = getenv("TABLE_PREFIX", "Swastika_")

T_SUDOERS = f"{TABLE_PREFIX}sudoers"


async def init_db() -> bool:
    global _pool
    if not DB_HOST or not DB_USER or not DB_PASSWORD:
        log.warning("DB not configured — sudo will be memory-only")
        return False
    try:
        _pool = await asyncpg.create_pool(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            min_size=1,
            max_size=4,
            command_timeout=30,
            timeout=15,
            ssl="require",
            statement_cache_size=0,
        )
        async with _pool.acquire() as conn:
            await conn.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {T_SUDOERS} (
                    id      TEXT PRIMARY KEY DEFAULT 'sudo',
                    sudoers BIGINT[] DEFAULT '{{}}'
                );
                """
            )
            await conn.fetchval("SELECT 1")
        log.warning("✅ DB connected (prefix=%s)", TABLE_PREFIX)
        return True
    except Exception as e:
        log.warning("⚠️ DB connect failed: %s — sudo memory-only", e)
        _pool = None
        return False


def _ok() -> bool:
    return _pool is not None


async def load_sudoers(owner_id: int) -> List[int]:
    """Load sudo list from DB. Always includes owner."""
    ids: Set[int] = set()
    if owner_id:
        ids.add(int(owner_id))
    if not _ok():
        return list(ids)
    try:
        async with _pool.acquire() as conn:
            row = await conn.fetchrow(
                f"SELECT sudoers FROM {T_SUDOERS} WHERE id='sudo'"
            )
        if row and row["sudoers"]:
            for x in row["sudoers"]:
                ids.add(int(x))
    except Exception as e:
        log.warning("load_sudoers failed: %s", e)
    return list(ids)


async def save_sudoers(sudoers: List[int], owner_id: int) -> bool:
    """Persist full sudo list to DB."""
    if not _ok():
        return False
    ids = list({int(x) for x in sudoers if x})
    if owner_id and int(owner_id) not in ids:
        ids.append(int(owner_id))
    try:
        async with _pool.acquire() as conn:
            await conn.execute(
                f"""
                INSERT INTO {T_SUDOERS}(id, sudoers) VALUES('sudo', $1)
                ON CONFLICT(id) DO UPDATE SET sudoers=EXCLUDED.sudoers
                """,
                ids,
            )
        return True
    except Exception as e:
        log.warning("save_sudoers failed: %s", e)
        return False
