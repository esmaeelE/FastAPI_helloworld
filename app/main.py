import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi_offline import FastAPIOffline

from app.config import settings
from app.routes import router
from app.scalar import scalar_docs


def configure_logging() -> None:
    logging.basicConfig(
        level=settings.log_level.upper(),
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@asynccontextmanager
async def lifespan(_app: FastAPIOffline) -> AsyncIterator[None]:
    configure_logging()
    logging.getLogger(__name__).info(
        "%s v%s (%s)", settings.app_name, settings.app_version, settings.app_env
    )
    yield
    logging.getLogger(__name__).info("shutdown")


app = FastAPIOffline(
    title=settings.app_name,
    description="Clean FastAPI service",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "docExpansion": "none",
    },
)

app.include_router(router)
scalar_docs(app)
