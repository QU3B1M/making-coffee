import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from tortoise.contrib.test import finalizer, initializer

from app.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        initializer(settings.DATABASE_MODELS, db_url=settings.DATABASE_URL)
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")
    finalizer() # Close DB connection


if __name__ == "__main__":
    main()
