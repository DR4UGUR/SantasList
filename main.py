from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.progress import track
from rich.progress import Progress
import time

'''
themes = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=themes)
print("[italic red]Hello[/italic red] World!")
console.print("Link", style="bold blue underline")
console.print([1, 2, 3])
console.log("Test")
console.print("info", style="info")
console.print("warning", style="warning")
console.print("danger", style="danger")
console.print(Panel("Hello, [red]World!"))
'''

with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
