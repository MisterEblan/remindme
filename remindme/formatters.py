from datetime import datetime

class DateTimeFormatter:
    def day(self, date: datetime) -> str:
        """
        Returns string in format dd-mm-yyyy
        """

        day = f"0{date.day}" if date.day < 10 else date.day
        month = f"0{date.month}" if date.month < 10 else date.month

        return f"{day}-{month}-{date.year}"

    def time(self, date: datetime) -> str:
        """
        Returns string in format hh-mm
        """

        hour = f"0{date.hour}" if date.hour < 10 else date.hour
        minute = f"0{date.minute}" if date.minute < 10 else date.minute

        return f"{hour}-{minute}"
