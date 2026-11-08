import os
import json
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


def save_entry(problem: str, answer: str) -> str:
    entry = json.dumps({"problem": problem, "answer": answer})
    code = (
        "import json\n"
        f"entry = json.loads({entry!r})\n"
        "with open('notebook.jsonl', 'a') as f:\n"
        "    f.write(json.dumps(entry) + '\\n')\n"
        "print('saved')"
    )
    return run_python(code)


def read_notebook() -> str:
    return run_python(
        "import os\n"
        "print(open('notebook.jsonl').read() if os.path.exists('notebook.jsonl') else '(empty)')"
    )