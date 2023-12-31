import typer
from src.utils import date_helper
from rich.console import Console
from web3 import Web3

app = typer.Typer()
console = Console()


@app.command(help="convert input str to lower case")
def lc(x: str):
    print(x.lower())


@app.command(help="convert input str to UPPER case")
def uc(x: str):
    print(x.upper())


@app.command(help="convert input str to checksum address")
def cs(x: str):
    try:
        print(Web3.to_checksum_address(x))
    except ValueError:
        console.print_exception(show_locals=True)


@app.command(help="convert timestamp to date string in local timezone")
def ts_to_date(timestamp: int):
    print(date_helper.timestamp_to_datestr(timestamp))


@app.command(help="convert date string to timestamp in local timezone")
def date_to_ts(date_str: str):
    print(date_helper.datestr_to_timestamp(date_str))
