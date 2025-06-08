def extract_jwt_token_from_header(auth_header_value):
  if not auth_header_value:
    return None
  token_parts = auth_header_value.split()
  if len(token_parts) != 2 or token_parts[0] != "Bearer":
    return None
  return token_parts[1]
