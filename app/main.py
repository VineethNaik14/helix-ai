from fastapi import FastAPI

app = FastAPI(
    title="Helix AI", description="AI Code Intelligence Platform", version="0.1.0"
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Helix - AI"}


@app.get("/health", tags=["Health"])
async def health():
    return {"Status": "Healthy"}
