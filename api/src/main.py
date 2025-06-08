from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.reports import report_router
from config import settings
from middleware.auth import check_auth

app = FastAPI()

# Добавление middleware проверки аутентификации
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
  try:
    check_auth(request)
  except HTTPException as error:
    return JSONResponse(status_code=error.status_code, content=error.detail)
  return await call_next(request)

# Добавление middleware CORS, разрешается origin фронтенда
app.add_middleware(
  CORSMiddleware,
  allow_origins=[settings.REACT_APP_URL],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(report_router)
