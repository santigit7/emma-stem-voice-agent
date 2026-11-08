import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from daytona_tool import run_python, get_sandbox, save_entry, read_notebook

load_dotenv()
SECRET = os.environ["SERVER_SECRET"]

app = FastAPI()
get_sandbox()


def check(x_secret):
    if x_secret != SECRET:
        raise HTTPException(status_code=401, detail="Bad secret")


class CodeRequest(BaseModel):
    code: str


class NoteRequest(BaseModel):
    problem: str
    answer: str


@app.post("/run")
def run(req: CodeRequest, x_secret: str = Header(None)):
    check(x_secret)
    return {"result": run_python(req.code)}


@app.post("/save")
def save(req: NoteRequest, x_secret: str = Header(None)):
    check(x_secret)
    return {"result": save_entry(req.problem, req.answer)}


@app.get("/notebook")
def notebook(x_secret: str = Header(None)):
    check(x_secret)
    return {"notebook": read_notebook()}