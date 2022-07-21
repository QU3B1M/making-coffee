from fastapi import APIRouter
 
from . import coffee_brew, coffee_maker


router = APIRouter(prefix='/api')

router.include_router(coffee_maker.router, tags=['coffee_maker'])
router.include_router(coffee_brew.router, tags=['coffee_brew'])
