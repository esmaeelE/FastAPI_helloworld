# myfastapiapp

> Clean FastAPI service with offline static assets.

## Quick Start

```bash
# prerequisites: uv, python 3.13+
uv sync
uv run uvicorn app.main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) — returns `{"message": "Hello World"}`

Interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Hello World |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc |
| GET | `/scalar` | Scalar API docs |

## Project Structure

```
app/
  __init__.py    # exports app instance
  config.py      # pydantic-settings config
  main.py        # FastAPI app + lifespan + logging
  routes.py      # endpoints
  scalar.py      # Scalar API docs integration
tests/
  conftest.py    # async client fixture
  test_routes.py # endpoint tests
pyproject.toml   # deps + scripts
Dockerfile       # multi-stage build
```

## Stack

- [FastAPI](https://fastapi.tiangolo.com/) via [fastapi-offline](https://github.com/mrtchz/fastapi-offline) (bundled static assets, no CDN)
- [Scalar](https://github.com/scalar/scalar) API docs
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for env config
- [Uvicorn](https://www.uvicorn.org/) ASGI server
- [uv](https://docs.astral.sh/uv/) package manager
- Python 3.13+

## Environment Variables

All variables are prefixed with `APP_`:

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_APP_NAME` | `My API` | Application name |
| `APP_APP_VERSION` | `1.0.0` | Application version |
| `APP_APP_ENV` | `development` | Environment |
| `APP_LOG_LEVEL` | `INFO` | Logging level |

## Testing

```bash
uv run pytest -v
```

## Docker

```bash
docker build -t myfastapiapp .
docker run -p 8000:8000 myfastapiapp
```

## TODO

- [x] Offline (bundled static assets)
- [x] Scalar
- [x] Tests (pytest + httpx)
- [x] Docker (Dockerfile + .dockerignore)
- [ ] CI (GitHub Actions: lint + test)
- [x] Health check endpoint (`GET /health`)
- [x] Structured logging
- [x] pydantic-settings for env config
