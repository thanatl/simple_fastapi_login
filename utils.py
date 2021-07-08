from fastapi import HTTPException, Header

def get_token_auth_header(authorization):
    parts = authorization.split()

    if parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=401, 
            detail='Authorization header must start with Bearer')
    elif len(parts) == 1:
        raise HTTPException(
            status_code=401, 
            detail='Authorization token not found')
    elif len(parts) > 2:
        raise HTTPException(
            status_code=401, 
            detail='Authorization header be Bearer token')
    
    token = parts[1]
    return token