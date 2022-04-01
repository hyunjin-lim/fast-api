from fastapi import FastAPI, Response, Request
from app.core.routers import api_router
from app.core.settings import settings
from starlette.middleware.cors import CORSMiddleware
from loguru import logger
import random
import uuid
import contextvars
from fastapi.responses import JSONResponse

request_id_contextvar = contextvars.ContextVar("request_id", default=None)

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


app.include_router(api_router, prefix=settings.api_prefix)




