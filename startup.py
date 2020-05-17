from rich.console import Console

console = Console()


def startup():
    console.print(r"""


     _____             _              _     _     _   
    /  ___|           | |            | |   (_)   | |  
    \ `--.  __ _ _ __ | |_ __ _ ___  | |    _ ___| |_ 
     `--. \/ _` | '_ \| __/ _` / __| | |   | / __| __|
    /\__/ / (_| | | | | || (_| \__ \ | |___| \__ \ |_ 
    \____/ \__,_|_| |_|\__\__,_|___/ \_____/_|___/\__|


                                                      """)
    console.print(
        "Welcome to [red] Santas List [/] of naughty passwords. I will ask you a few questions about the target "
        "and then make a dictionary of passwords using all the information I have. [underline]Leave the "
        "information you dont have blank[/] "
    )
    console.print(r"""


    """)
