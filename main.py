from fastapi import FastAPI
from database import Base,engine
from routes import users,posts,login
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:4200",  # Angular Dev Server
    "http://127.0.0.1:4200"  # Sometimes Angular runs here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


Base.metadata.create_all(engine)

@app.get("/")  # Make sure this route exists
def read_root():
    return {"message": "Hello from FastAPI on Replit!"}

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(login.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
