from utils.formatters import DateTimeFormatter
from utils.cli import RemindMeCLI
formatter = DateTimeFormatter()
def test_run():
    cli = RemindMeCLI("./remindme", formatter)
    idea = "implement convolution"
    cli.run([idea])
    with open("./remindme/06-07-2025.txt", "r") as file:
        line = file.readline()
    assert line
