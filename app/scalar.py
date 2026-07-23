from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


def scalar_docs(app: FastAPI) -> None:
    @app.get("/scalar", include_in_schema=False)  # type: ignore[misc]
    async def scalar_html():  # noqa: ANN202
        return get_scalar_api_reference(
            openapi_url=app.openapi_url,
            title=app.title,
        )
