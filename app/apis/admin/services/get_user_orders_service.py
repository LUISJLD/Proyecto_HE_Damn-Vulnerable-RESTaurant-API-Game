from fastapi import APIRouter, Depends
from db.session import get_db
from sqlalchemy.orm import Session
from apis.auth.utils import get_current_user
from typing_extensions import Annotated
from db.models import User, Order

router = APIRouter()

@router.get("/admin/user-orders/{user_id}")
def get_user_orders(
    user_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    # VULNERABILIDAD INTENCIONAL:
    # No valida que el usuario tenga rol de ADMIN
    # No valida que user_id corresponda al usuario autenticado

    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return {
        "message": "Confidential orders retrieved successfully",
        "orders": orders,
        "requested_for_user_id": user_id,
        "current_user_role": current_user.role,
    }
