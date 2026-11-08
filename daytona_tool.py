import os
from dotenv import load_dotenv
from daytona import Daytona, DaytonaConfig

load_dotenv()

daytona = Daytona(DaytonaConfig(api_key=os.environ["DAYTONA_API_KEY"]))
_sandbox = None


def get_sandbox():
    global _sandbox
    if _sandbox is None:
        _sandbox = daytona.create()
    return _sandbox


def run_python(code: str) -> str:
    global _sandbox
    try:
        return get_sandbox().process.code_run(code).result
    except Exception:
        _sandbox = None
        return get_sandbox().process.code_run(code).result