from prefect import flow
from prefect.runner.storage import GitRepository

if __name__ == "__main__":
    source = GitRepository(
        url="https://github.com/axelstudios/prefect-test.git",
    )

    flow.from_source(source=source, entrypoint="main.py:greet_user").deploy(
        name="github-deploy",
        work_pool_name="My Pool",
    )
