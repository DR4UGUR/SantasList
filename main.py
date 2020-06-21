from PyInquirer import prompt
from rich.console import Console
import startup
console = Console()
startup.startup()
want_guide = prompt(
        {
            "type": "input",
            "name": "guided",
            "message": "Do you want to use a guided creation or do you want to go unguided? (G/U)",
        }
)
if want_guide["guided"] == "G":
    startup.guided()
elif want_guide["guided"] == "U":
    startup.unguided()
else:
    print("Please enter G or U for guided or unguided")
