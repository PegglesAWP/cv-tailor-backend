from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title="CV Tailor",
    description="API for generating tailored CVs and cover letters",
    version="0.1.0",
    docs_url="/docs" if settings.DEBUG else None,
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["<http://localhost:3000>", "<http://localhost:5173>"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to CV Tailor API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Error handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    if settings.DEBUG:
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)},
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."},
    )

# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
