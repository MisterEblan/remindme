from datetime import datetime
import os
from .formatters import DateTimeFormatter

class FileManager:
    def __init__(self, path: str, formatter: DateTimeFormatter):
        self._directory: str = path
        self._formatter: DateTimeFormatter = formatter

    @property
    def directory(self) -> str:
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


        if not os.path.exists(f"{file_name}"):

            print(f"Creating {file_name}")

            with open(f"{file_name}", "w") as file:
                file.write("")

        else:
            raise RuntimeError("File already exists")

    def write(self, idea: str) -> None:
        """
        Writes idea to today's file
        """

        file_name = self._get_file_name()
        time = self._get_time()

        with open(file_name, "a") as file:
            file.write(f"{time} | {idea}\n")

    def _get_file_name(self) -> str:
        date = datetime.now()

        return f"{self._directory}/{self._formatter.day(date)}.txt"

    def _get_time(self) -> str:
        # TODO: implement datetime.now
        date = datetime.now()

        # date = datetime(2025, 7, 6, 19, 00)

        return self._formatter.time(date)
