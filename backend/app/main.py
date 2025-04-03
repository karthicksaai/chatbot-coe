from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes.chat import router as chat_router
from .config.database import connect_to_mongodb, close_mongodb_connection

app = FastAPI(title="COE Chatbot API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongodb()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongodb_connection()

# Include routers
app.include_router(chat_router, tags=["chat"])

@app.get("/")
async def root():
    return {"message": "COE Chatbot API is running"}
