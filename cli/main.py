import datetime as dt
import typer

from cli.helper import save_input

app = typer.Typer()


@app.command()
def today():
    """
    Get the question of today.
    """
    today = dt.datetime.today()
    year = today.year
    day = today.day
    save_input(year, day)


@app.command()
def yay():
    pass


if __name__ == "__main__":
    app()
