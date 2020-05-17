from PyInquirer import prompt
from rich.console import Console
from startup import startup
import questions
console = Console()
startup()

answers = prompt(questions.questions)
console.print(answers)
