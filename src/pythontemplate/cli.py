import typer
from loguru import logger

app = typer.Typer()


@app.command()
def main() -> None:
    logger.info("Hello, world!")
