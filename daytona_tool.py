from daytona import Daytona, DaytonaConfig

config = DaytonaConfig(api_key="dtn_1c75dd97e7cd704f536516bb3526ace27d8ae79461f6b89e4e50a7719a92e104")
daytona = Daytona(config)


def run_python(code: str) -> str:
    sandbox = daytona.create()
    try:
        response = sandbox.process.code_run(code)
        return response.result
    finally:
        sandbox.delete()


if __name__ == "__main__":
    # Molar mass of water (H2O) = 2 hydrogens + 1 oxygen
    print(run_python("print(2 * 1.008 + 15.999)"))