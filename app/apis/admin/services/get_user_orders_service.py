from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db
from sqlalchemy.orm import Session
from apis.auth.utils import get_current_user
from typing_extensions import Annotated
from db.models import UserRole
from db.models import User, Order

router = APIRouter()

@router.get("/admin/user-orders/{user_id}")
def get_user_orders(
    user_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):

    # Validación de control de acceso basada en roles (RBAC) y propiedad del recurso
    if current_user.role != UserRole.CHEF.value and current_user.id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Unauthorized access: You cannot view other users' orders"
        )

    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return {
        "message": "Orders retrieved successfully",
        "orders": orders,
        "requested_for_user_id": user_id,
        "current_user_role": current_user.role,
    }