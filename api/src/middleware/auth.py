from fastapi import Request, HTTPException
from keycloak import KeycloakOpenID

from config import settings
from utils.jwt import extract_jwt_token_from_header

keycloak_openid = KeycloakOpenID(
  server_url=settings.KEYCLOAK_SERVER_URL,
  realm_name=settings.KEYCLOAK_REALM_NAME,
  client_id=settings.KEYCLOAK_CLIENT_ID
)

# Middleware для проверки JWT токена и наличия роли
def check_auth(request: Request):
  auth_header_value = request.headers.get("Authorization")
  auth_token = extract_jwt_token_from_header(auth_header_value)

  if not auth_token:
    raise HTTPException(status_code=401, detail="Invalid token")

  # Верификация токена
  payload = None
  try:
    # валидируется с помощью публичного ключа благодаря флагу validate=True
    payload = keycloak_openid.decode_token(auth_token, validate=True)
  except Exception:
    raise HTTPException(status_code=401, detail="Invalid token")
  
  # Проверка роли
  if payload:
    current_user_roles = payload.get("realm_access", {}).get("roles", [])
    # делается пересечение ролей пользователя и разрешенных ролей, если есть - права предоставляются
    current_user_allowed_roles = list(set(current_user_roles) & set(settings.KEYCLOAK_ROLES_TO_ALLOW))
    if len(current_user_allowed_roles) == 0:
      raise HTTPException(status_code=403, detail="Permission denied")
