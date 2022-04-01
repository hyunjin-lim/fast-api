from fastapi import FastAPI, Response, Request, Depends
from app.core.routers import api_router
from app.core.settings import settings
from starlette.middleware.cors import CORSMiddleware
from loguru import logger
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(**settings.fastapi_kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_request(request, call_next):
    logger.info(f'{request.method} {request.url}')
    response = await call_next(request)
    logger.info(f'Status code: {response.status_code}')
    body = b""
    async for chunk in response.body_iterator:
        body += chunk
    # do something with body ...
    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/test")
def read_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


app.include_router(api_router, prefix=settings.api_prefix)


