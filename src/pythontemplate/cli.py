import logging

import typer

logger = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main() -> None:
    format_str = "%(asctime)s | %(levelname)s | %(name)s:%(lineno)d - %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO)
    logger.info("Hello, world!")
