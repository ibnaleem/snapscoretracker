"""
Created by: https://github.com/ibnaleem
Repository: https://github.com/ibnaleem/snapscoretracker
"""

from typing import Union
from rich.console import Console
import argparse, datetime, numpy as np, pandas as pd, os, re

class SnapscoreTracker:
    def __init__(self) -> None:
        self.directory = "logs"
        self.console = Console()
        self.date = datetime.datetime.utcnow()

    def calculate_time_difference(self, previous_date: Union[str, datetime.datetime], custom_date=None) -> str:
        """
        Calculates time difference between the given date and the current time (UTC).

        Args:
            previous_date (Union[str, datetime.datetime]): The previous date in string format or as a datetime object.
            custom_date (optional): the custom date to subtract from

        Returns:
            str: A string describing the time difference.
        """
        if custom_date:
            now = datetime.datetime.strptime(custom_date, "%Y-%m-%d %H:%M:%S")
        else:
            now = datetime.datetime.utcnow()

        if isinstance(previous_date, str):
            date_object = datetime.datetime.strptime(previous_date, "%Y-%m-%d %H:%M:%S")
        else:
            date_object = previous_date

        time_difference = now - date_object

        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        time_diff_str = ""

        if days > 0:
            time_diff_str += f"{days} days, "
        if hours > 0:
            time_diff_str += f"{hours} hours, "
        if minutes > 0:
            time_diff_str += f"{minutes} minutes, "
        if seconds > 0 or time_diff_str == "":
            time_diff_str += f"{seconds} seconds"
        else:
            time_diff_str = time_diff_str.rstrip(", ")

        return time_diff_str

    def create_dir(self, username: str, snapscore: int, custom_date=None):
        file_path = f"{self.directory}/{username.lower()}_logs.csv"
        try:
            os.makedirs(self.directory)
            open(file_path, "w").close()
        except FileExistsError:
            open(file_path, "w").close()
        
        if not custom_date:
            self.add_row(username, snapscore)
        else:
            self.add_row(username, snapscore, custom_date)

    def add_row(self, username: str, snapscore: int, custom_date=None) -> None:
        file_path = f"{self.directory}/{username.lower()}_logs.csv"
        columns = [
            "Date",
            "Time Difference",
            "Snapscore",
            "Increase",
            "Increase Difference",
            "Snaps Sent",
            "Number of Snaps Sent Since Last Time",
            "Snaps Opened",
            "Number of Snaps Opened Since Last Time",
            "Number of People Snapped",
            "Number of People Snapped Since Last Time",
        ]

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path)
        else:
            if not custom_date:
                self.create_dir(username, snapscore)
            else:
                self.create_dir(username, snapscore, custom_date)
        if df.empty:
            new_row = {
                "Date": self.date,
                "Snapscore": snapscore,
                "Increase": "Initial, no increase",
                "Snaps Sent": 0,
                "Snaps Opened": 0,
                "Number of People Snapped": 0,
                "Time Difference": "",
                "Increase Difference": "",
                "Number of Snaps Sent Since Last Time": "",
                "Number of Snaps Opened Since Last Time": "",
                "Number of People Snapped Since Last Time": "",
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            self.console.print(
                f"[bold green]✅ Initialised new row in {file_path}\nDatetime: {self.date.strftime('%Y-%m-%d %H:%M:%S')}\nSnapscore: {snapscore}\nIncrease: Initial, no increase\nSnaps sent: {snapscore // 2}\nSnaps opened: {snapscore % 2}\nNumber of People Snapped: {snapscore // 2}[/bold green]"
            )
            df.to_csv(file_path, index=False)

        else:
            last_row = df.iloc[-1]
            prev_datetime = last_row["Date"]
            prev_snapscore = last_row["Snapscore"]
            prev_increase = (
                int(last_row["Increase"])
                if last_row["Increase"] != "Initial, no increase"
                else 0
            )
            prev_snaps_sent = last_row["Snaps Sent"]
            prev_snaps_opened = last_row["Snaps Opened"]
            prev_amount_of_ppl_snapped = last_row["Number of People Snapped"]

            if custom_date:
                datetime_diff = self.calculate_time_difference(
                    prev_datetime, custom_date=custom_date
                )
                self.date = datetime.datetime.strptime(custom_date, "%Y-%m-%d %H:%M:%S")
            else:
                datetime_diff = self.calculate_time_difference(prev_datetime)
            increase = snapscore - prev_snapscore
            increase_diff = increase - prev_increase
            snaps_sent = increase // 2
            snaps_sent_diff = snaps_sent - prev_snaps_sent
            snaps_opened = (increase // 2) + (increase % 2)
            snaps_opened_diff = snaps_opened - prev_snaps_opened
            amount_of_ppl_snapped = increase // 2
            diff_in_num_ppl_snapped = amount_of_ppl_snapped - prev_amount_of_ppl_snapped

            new_row = {
                "Date": self.date,
                "Time Difference": datetime_diff,
                "Snapscore": snapscore,
                "Increase": increase,
                "Increase Difference": int(increase_diff),
                "Snaps Sent": int(snaps_sent),
                "Number of Snaps Sent Since Last Time": int(snaps_sent_diff),
                "Snaps Opened": int(snaps_opened),
                "Number of Snaps Opened Since Last Time": int(snaps_opened_diff),
                "Number of People Snapped": int(amount_of_ppl_snapped),
                "Number of People Snapped Since Last Time": int(
                    diff_in_num_ppl_snapped
                ),
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(file_path, index=False)
            self.console.print(f"[bold green]✅ Added new row in {file_path}\nDate: {self.date.strftime('%Y-%m-%d %H:%M:%S')}\nTime Difference: {datetime_diff}\nSnapscore: {snapscore}\nIncrease: {increase}\nIncrease Difference: {int(increase_diff)}\nSnaps Sent: {int(snaps_sent)}\nNumber of Snaps Sent Since Last Time: {int(snaps_sent_diff)}\nSnaps Opened: {int(snaps_opened)}\nNumber of Snaps Opened Since Last Time: {int(snaps_opened_diff)}\nNumber of People Snapped: {int(amount_of_ppl_snapped)}\nNumber of People Snapped Since Last Time: {int(diff_in_num_ppl_snapped)}[/bold green]")
            self.calculate_snap_rate_per_min(username)
            self.calculate_snap_rate_per_hour(username)
            self.calculate_snap_rate_per_day(username)

    def convert_to_minutes(self, time_diff) -> int:
        if pd.isna(time_diff):
            return 0
        minutes = 0

        hours_match = re.search(r'(\d+)\s*hours?', time_diff)
        minutes_match = re.search(r'(\d+)\s*minutes?', time_diff)
        if hours_match:
            minutes += int(hours_match.group(1)) * 60
        if minutes_match:
            minutes += int(minutes_match.group(1))
        return minutes

    def calculate_snap_rate_per_min(self, username: str):
        file_path = f"{self.directory}/{username.lower()}_logs.csv"        
        df = pd.read_csv(file_path)

        df['time_minutes'] = df['Time Difference'].apply(self.convert_to_minutes)
        df['increase'] = pd.to_numeric(df['Increase'], errors='coerce').fillna(0)

        df['Snap Rate / min'] = np.nan

        total_minutes = 0
        total_snaps = 0

        for i in range(len(df)):
            total_minutes += df.at[i, 'time_minutes']
            total_snaps += df.at[i, 'increase']

            if total_minutes >= 1:
                df.at[i, 'Snap Rate / min'] = total_snaps / total_minutes
                total_minutes = 0
                total_snaps = 0

        df = df.drop(['time_minutes', 'increase'], axis=1)

        df.to_csv(file_path, index=False)

        self.console.print("[bold green]✅ Calculated Snap rate per minute[/bold green]")

    def calculate_snap_rate_per_hour(self, username: str):
        file_path = f"{self.directory}/{username.lower()}_logs.csv"
        df = pd.read_csv(file_path)

        df['time_minutes'] = df['Time Difference'].apply(self.convert_to_minutes)
        df['increase'] = pd.to_numeric(df['Increase'], errors='coerce').fillna(0)

        df['Snap Rate / hour'] = np.nan

        total_minutes = 0
        total_snaps = 0
        for i in range(len(df)):
            total_minutes += df.at[i, 'time_minutes']
            total_snaps += df.at[i, 'increase']

            if total_minutes >= 60:
                df.at[i, 'Snap Rate / hour'] = total_snaps / (total_minutes / 60)
                total_minutes = 0
                total_snaps = 0

        df.to_csv(file_path, index=False)
        self.console.print("[bold green]✅ Calculated Snap rate per hour[/bold green]")
        df = df.drop('time_minutes', axis=1)
        df = df.drop('increase', axis=1)
        df.to_csv(file_path, index=False)

    def calculate_snap_rate_per_day(self, username: str):
        file_path = f"{self.directory}/{username.lower()}_logs.csv"
        df = pd.read_csv(file_path)

        df['time_minutes'] = df['Time Difference'].apply(self.convert_to_minutes)
        df['increase'] = pd.to_numeric(df['Increase'], errors='coerce').fillna(0)

        df['Snap Rate / day'] = np.nan

        total_minutes = 0
        total_snaps = 0
        for i in range(len(df)):
            total_minutes += df.at[i, 'time_minutes']
            total_snaps += df.at[i, 'increase']

            if total_minutes >= 1440:  # 1440 minutes in a day
                df.at[i, 'Snap Rate / day'] = total_snaps / (total_minutes / 1440)
                total_minutes = 0
                total_snaps = 0

        df.to_csv(file_path, index=False)
        self.console.print("[bold green]✅ Calculated Snap rate per day[/bold green]")
        df = df.drop('time_minutes', axis=1)
        df = df.drop('increase', axis=1)
        df.to_csv(file_path, index=False)

    def average(self, username: str, column: str):
        file_path = f"{self.directory}/{username.lower()}_logs.csv"
        df = pd.read_csv(file_path)

        mean = df[column].mean()

        self.console.print(f"[bold green]Average {column}: {mean}[/bold green]")
def main():
    parser = argparse.ArgumentParser(
        prog="Snapscore Tracker",
        description="👻 A Snapscore tracker that reports various metrics such as time differences, score increases, snaps sent and received, snap rates per minute, hour, and day and much more.",
        epilog="Contribute: https://github.com/ibnaleem/snapscoretracker"
    )

    parser.add_argument("-u", "--username", type=str, help="Snapchat username to track", required=True)
    parser.add_argument("-s", "--snapscore", type=int, help="Snapscore to log", required=False)
    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="The time you want to log the Snapscore in Y-m-d H:M:S format.\nExample: 2024-06-15 12:00:00 will log the Snapscore at 12:00:00 on June 15, 2024.\nIf not provided, the current time will be used. Use this feature if you want to log the Snapscore at a specific time.\nWARNING: Current time can be inaccurate by an hour: 2024-06-15 12:00:00 will log the Snapscore at 11:00:00 on June 15, 2024. Using this parameter will fix this issue.",
        required=False
    )

    parser.add_argument("-a", "--average", type=str, help="Calculate the mean of a column from the logs", required=False)

    args = parser.parse_args()

    tracker = SnapscoreTracker()

    if args.time and args.snapscore:
        tracker.add_row(args.username, args.snapscore, custom_date=args.time)
    elif args.snapscore:
        tracker.add_row(args.username, args.snapscore)
    
    if args.average and not args.snapscore:
        tracker.average(args.username, args.average)

if __name__ == "__main__":
    main()
