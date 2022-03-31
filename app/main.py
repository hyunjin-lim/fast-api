from fastapi import FastAPI
from app.core.routers import api_router
from app.core.settings import settings
from starlette.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    # settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()

