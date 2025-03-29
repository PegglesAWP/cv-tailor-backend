from fastapi import APIRouter

from app.api.v1.endpoints import auth, users, experiences, documents, employers

api_router = APIRouter()

# Include all the API routes
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(experiences.router, prefix="/profile", tags=["profile"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(employers.router, prefix="/employers", tags=["employers"])