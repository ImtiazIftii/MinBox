from fastapi import FastAPI

from minbox_api.core.config import settings

# 1st we create the FASTAPI instance
# using the title and version definec in our config file

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
)


@app.get(
    f"{settings.API_V1_STR}/health",
    tags=["Health"],
    summary="Health Check",
    description="Returns the current operational status and the version of the API",
)
async def health_check() -> dict[str, str]:
    """liveness probe endpoint. used by docker,
    load balancers to confirm the api's health
    """

    return {
        "status": "healthy",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }
