from fastapi import APIRouter
 
from . import auth, coffee_brew, coffee_maker


router = APIRouter(prefix='/api')

router.include_router(auth.router, tags=['auth'])
router.include_router(coffee_maker.router, tags=['coffee_maker'])
router.include_router(coffee_brew.router, tags=['coffee_brew'])
