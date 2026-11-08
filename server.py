import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from daytona_tool import run_python

load_dotenv()
SECRET = os.environ["SERVER_SECRET"]

app = FastAPI()


class CodeRequest(BaseModel):
    code: str


@app.post("/run")
def run(req: CodeRequest, x_secret: str = Header(None)):
    if x_secret != SECRET:
        raise HTTPException(status_code=401, detail="Bad secret")
    return {"result": run_python(req.code)}