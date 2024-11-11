import argparse
import time
from datetime import datetime, timedelta

from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def format_time(seconds):
    return str(timedelta(seconds=seconds))


def countdown(timer_type, duration, sessions, current_index):
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration)

    console.clear()
    display_future_sessions(sessions, current_index)
    console.print(
        f"\n[bold blue]{timer_type}[/bold blue] session started, will end at: [green]{end_time.strftime('%H:%M')}[/green]\n",
        justify="center",
    )

    while datetime.now() < end_time:
        remaining_seconds = int((end_time - datetime.now()).total_seconds())
        console.print(
            format_time(remaining_seconds),
            end="\r",
            style="bold yellow",
            # justify="center", # issue: does not overwrite the previous time left!
        )
        time.sleep(1)

    console.print(
        f"\n[bold red]{timer_type} session ended.[/bold red]\n",
        justify="center",
    )


def calculate_future_sessions(work_duration, break_duration, number_of_sessions):
    now = datetime.now()
    sessions = []
    for i in range(number_of_sessions):
        work_end_time = now + timedelta(minutes=work_duration)
        sessions.append(("Work", work_end_time.strftime("%H:%M"), i * 2))
        now = work_end_time + timedelta(minutes=break_duration)
        if i != number_of_sessions - 1:
            sessions.append(("Break", now.strftime("%H:%M"), i * 2 + 1))
    return sessions


def display_future_sessions(sessions, current_index):
    table = Table(title="Pomodoro Sessions", box=box.ROUNDED)
    table.add_column("Session #", justify="center", style="cyan")
    table.add_column("Type", justify="center", style="magenta")
    table.add_column("Ends At", justify="center", style="green")
    table.add_column("Current?", justify="center", style="red")

    last_session_number = None
    for i, (session_type, end_time, _) in enumerate(sessions):
        session_number = (i // 2) + 1
        session_number_display = (
            str(session_number)
            if session_type == "Work" and session_number != last_session_number
            else ""
        )
        last_session_number = (
            session_number if session_type == "Work" else last_session_number
        )

        marker = "x" if i == current_index else ""
        table.add_row(session_number_display, session_type, end_time, marker)

    console.print(table, justify="center")


def main():
    parser = argparse.ArgumentParser(description="pomodoro-endtimes CLI")
    parser.add_argument(
        "-w",
        "--work",
        type=int,
        default=40,
        help="Length of work session in minutes",
    )
    parser.add_argument(
        "-b",
        "--break_time",
        type=int,
        default=5,
        help="Length of break session in minutes",
    )
    parser.add_argument(
        "-n",
        "--next_sessions",
        type=int,
        default=4,
        help="Number of future sessions to display",
    )

    args = parser.parse_args()

    try:
        sessions = calculate_future_sessions(
            args.work,
            args.break_time,
            args.next_sessions,
        )
        current_session_index = 0
        while True:
            if current_session_index >= len(sessions):
                current_session_index = 0
                sessions = calculate_future_sessions(
                    args.work, args.break_time, args.next_sessions
                )

            # Get the session type and duration
            session_type, _, index = sessions[current_session_index]
            duration = args.work if session_type == "Work" else args.break_time

            # Run the session
            countdown(session_type, duration, sessions, current_session_index)
            current_session_index += 1

    except KeyboardInterrupt:
        console.print("\n[bold red]Timer stopped.[/bold red]")


if __name__ == "__main__":
    main()
