"""
Endpoints for active announcements
"""

from datetime import datetime, timezone
from typing import Any, Dict, List

from fastapi import APIRouter

from ..database import announcements_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


@router.get("", response_model=List[Dict[str, Any]])
@router.get("/", response_model=List[Dict[str, Any]])
def get_active_announcements() -> List[Dict[str, Any]]:
    """Get announcements that have not expired."""
    now = datetime.now(timezone.utc)
    return list(announcements_collection.find(
        {"expires_at": {"$gt": now}},
        {"_id": 0, "message": 1, "expires_at": 1}
    ).sort("expires_at", 1))
