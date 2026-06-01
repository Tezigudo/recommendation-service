from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.route import router
from config import ALLOWED_ORIGINS, CORS_ALLOW_CREDENTIALS, DEBUG


app = FastAPI(debug=DEBUG)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(router)