from PyInquirer import prompt
from rich.console import Console
from startup import startup
import supplements
console = Console()
startup()

answers = prompt(supplements.questions)
console.print(answers)
