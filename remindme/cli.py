import argparse
import os
import pathlib
from datetime import datetime
from typing import List, Optional
from .file_manager import FileManager
from .formatters import DateTimeFormatter

class RemindMeCLI:
    def __init__(self, formatter: DateTimeFormatter,
                 path: str = f"{str(pathlib.Path.home())}/remindme"
                 ):
        self._file_manager = FileManager(path, formatter)
        self._formatter = formatter
        self._parser = argparse.ArgumentParser(
            prog="remindme",
            description="CLI tool for reminding some ideas that come up in a moment.",
            epilog="Example: remindme \"implement convolution\""
        )

        self._parser.add_argument(
            "idea",
            type=str,
            help="Idea itself"
        )

    def _parse_args(self, args: Optional[List[str]] = None):
        return self._parser.parse_args(args)

    def _format_idea(self, idea: str, date: datetime) -> str:
        time_str = self._formatter.time(date)

        return f"{time_str} | {idea}\n"

    def _save_idea(self, idea: str):
        self._file_manager.write(idea)

    def _is_file_exists(self):
        day_str = self._formatter.day(datetime.now())

        if os.path.exists(f"{self._file_manager.directory}/{day_str}.txt"):
            return True

        return False

    def run(self, args: Optional[List[str]] = None):

        if not self._is_file_exists():
            self._file_manager.mkdir()
            self._file_manager.create_file()

        try:
            parsed_args = self._parse_args(args)

            date = datetime.now()

            formatted_idea = self._format_idea(parsed_args.idea, date)

            self._save_idea(formatted_idea)

            print("Idea saved")

        except Exception as e:
            print(f"Something went wrong: {e}")

