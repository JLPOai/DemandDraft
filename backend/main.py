from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import motion_router

app = FastAPI(
    title="MotionForge AI - Legal Motion Drafting Engine",
    description="FastAPI Backend for Motion to Compel Document Drafting with Multi-Layer Agent Pipeline and Legal Web Search Layer.",
    version="1.0.0"
)

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(motion_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
