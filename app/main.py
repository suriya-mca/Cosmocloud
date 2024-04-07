from decouple import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from router import lms_router


# create fast-api instance
app = FastAPI(default_response_class=UJSONResponse)

# cors settings
origins = [
    '*',
]

# middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register router
app.include_router(
    lms_router.router,
    prefix="/api/v1"
)