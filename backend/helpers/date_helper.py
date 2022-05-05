from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def convert_date(date_str: str) -> str:
    return str(datetime.strptime(date_str, DATE_FORMAT))
