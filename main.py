from dataclasses import dataclass
from datetime import datetime
from typing import List

from date_filtering import rows_of_month
from extract import extract_rows
from read_logins import players_from_file
from scrap import scrape_login_records


@dataclass
class RecordCount:
    login: str
    nickname: str
    records_count: int

# year of records - ex. 2023
year = 2023
# month of records - 1-12
month = 7
# name of file with searched users' names 
file_path = "logins.txt"

if __name__ == '__main__':
    # Read logins.txt
    players = players_from_file(file_path)

    login_records_count: List[RecordCount] = []

    for player in players:
        # Get rows from all pages containing records after specified date
        rows = scrape_login_records(
            row_extract_strategy=extract_rows,
            login=player.login,
            until=datetime(year, month, 1)
        )

        # Filter records by month and year
        records = rows_of_month(rows, month, year)

        login_records_count.append(RecordCount(
            player.login, player.nickname, len(records)))

    # Sort users by most records descending
    login_records_count.sort(key=lambda x: x.records_count, reverse=True)

    # Print filtered out records
    for idx, record in enumerate(login_records_count):
        print(f'{idx+1}. {record.nickname} - {record.records_count}')
