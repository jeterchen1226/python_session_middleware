from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import secrets

SECRET_KEY = secrets.token_hex(32) 
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

@app.get("/hello")
def hello(request: Request, name):
    request.session["data"] = name
    return {"message": f"Hello,{name}"}

@app.get("/talk")
def talk(request: Request):
    if "data" in request.session:
        name = request.session["data"]
        return {"message": f"welcome,{name}"}
    else:
        return {"message": "你是誰？"}

app.mount("/", StaticFiles(directory="public", html=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
