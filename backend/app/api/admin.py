from fastapi import APIRouter, Depends
from app.core.deps import require_admin

router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.get("/dashboard", response_model=None)
def admin_dashboard(admin=Depends(require_admin)):
    return {
        "message": "Welcome admin",
        "admin_id": admin.id
    }
