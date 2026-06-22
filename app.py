from fastapi_offline import FastAPIOffline

app = FastAPIOffline()
app = FastAPIOffline(
    title="My API",
    description="Clean FastAPI service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "docExpansion": "none",
    },
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
