from fastapi import APIRouter

from app.api.health import health_check

router = APIRouter()

router.get("/health-check")(health_check)