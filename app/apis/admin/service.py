from apis.admin.services.get_disk_stats_service import router as get_disk_stats_router
from fastapi import APIRouter
from apis.admin.services.get_user_orders_service import router as user_orders_router
from apis.admin.services.reset_chef_password_service import (
    router as reset_chef_password_router,
)



router = APIRouter()
router.include_router(get_disk_stats_router)
router.include_router(reset_chef_password_router)
router.include_router(user_orders_router)

