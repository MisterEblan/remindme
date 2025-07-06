import os
import pathlib
from datetime import datetime
from .formatters import DateTimeFormatter

class FileManager:
    def __init__(self, path: pathlib.Path, formatter: DateTimeFormatter):
        self._directory: pathlib.Path = path
        self._formatter: DateTimeFormatter = formatter

    @property
    def directory(self) -> pathlib.Path:
        return self._directory

    def mkdir(self) -> None:
        """
        Creates a dir from path in init 
        """

        if not os.path.exists(self._directory):

            print(f"Creating {self._directory} dir")

            os.mkdir(self._directory)
        else:
            raise RuntimeError("Directory already exists")

    def create_file(self) -> None:
        """
        Creates a file with today's date in a dir from path in init
        """

        file_name = self._get_file_name()


        if not os.path.exists(file_name):

            print(f"Creating {file_name}")

            with open(file_name, "w") as file:
                file.write("")

        else:
            raise RuntimeError("File already exists")

    def write(self, idea: str) -> None:
        """
        Writes idea to today's file
        """

        print(f"Debug: Writing to file")

        file_name = self._get_file_name()
        time = self._get_time()
        formatted_idea = f"{time} | {idea}\n"

        with open(file_name, "a") as file:
            file.write(formatted_idea)
            print(f"Debug: {formatted_idea}")

    def _get_file_name(self) -> pathlib.Path:
        date = datetime.now()

        name: pathlib.Path = pathlib.Path(self._directory) / self._formatter.day(date)

        return name.with_suffix(".txt")

    def _get_time(self) -> str:
        date = datetime.now()

        return self._formatter.time(date)
