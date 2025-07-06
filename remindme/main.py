import sys
from .cli import RemindMeCLI
from .formatters import DateTimeFormatter

def main():

    if len(sys.argv) < 2:
        print("Idea not provided")
        sys.exit(-1)

    cli = RemindMeCLI(DateTimeFormatter())
    args = sys.argv[1:]

    print(f"Debug: {args}")

    try:
        cli.run(args)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(-1)


if __name__ == "__main__":
    main()
