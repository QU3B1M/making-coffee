# Third-party imports
from fastapi import APIRouter

# Making-cofee imports
from . import coffee_maker, maker_type


router = APIRouter(prefix="/api")

router.include_router(coffee_maker.router, tags=["coffee_maker"])
router.include_router(maker_type.router, tags=["maker_type"])
