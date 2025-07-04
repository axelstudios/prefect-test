from prefect import flow
from prefect.flow_runs import pause_flow_run
from prefect.logging import get_run_logger
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


@flow
async def greet_user():
    logger = get_run_logger()

    user = await pause_flow_run(wait_for_input=User)

    logger.info(f"Hello, {user.name}! 😉 Your age is {user.age}. 💥")
