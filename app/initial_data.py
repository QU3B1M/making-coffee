import json
import logging

from tortoise import Tortoise, run_async

from app.core.config import settings
from app.schemas import CoffeeMaker


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def load_default_coffee_makers() -> list[CoffeeMaker]:
    """Load initial data (default coffee makers) from a json file."""
    with open("app/static/default_makers.json", "r") as file:
        return json.load(file)


async def init() -> None:
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": settings.DATABASE_MODELS},
    )
    await Tortoise.generate_schemas()
    # Load and register defaults coffee makers.
    default_makers = await load_default_coffee_makers()
    [await CoffeeMaker.create(**maker) for maker in default_makers]


def main() -> None:
    logger.info("Creating initial data")
    run_async(init())
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
