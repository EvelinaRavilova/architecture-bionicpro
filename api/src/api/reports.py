from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .mocks import REPORTS_LIST

report_router = APIRouter()

@report_router.get("/reports")
async def get_reports():
  return JSONResponse(status_code=200, content=REPORTS_LIST)
