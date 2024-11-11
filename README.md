<p align="center">
  <img src="logo.jpg" width="100"/>
</p>

# pomodoro-endtimes
A minimalistic command-line Pomodoro timer application in Python. 

### Why?
A feature I was missing in most Pomodoro apps is to display the end time of the working session.
And a natural extension of that was: when will I end `N` pomodoro sessions (including breaks)?

### Features

- **Customize Work and Break Durations**: Adjust the length of your work and break sessions to suit your productivity pattern.
- **End Time Indicator**: Clearly see when each session will end, helping to plan your day effectively.
- **Session Table View**: A dynamic and informative representation of current and upcoming sessions, leveraging the beauty of the `rich` library.

### Requirements

Ensure you have Python installed (version 3.6 or above recommended) and the `rich` library.

Install `rich` using pip:
```bash
pip install rich
```

### Usage

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/yourusername/pomodoro-endtimes.git
cd pomodoro-endtimes
```

Run the Pomodoro timer script (`pet.py`) with customizable options:

```bash
python pet.py -w <work_duration> -b <break_duration> -n <next_sessions>
```

- **`-w, --work`**: Length of work session in minutes (default: 40)
- **`-b, --break_time`**: Length of break session in minutes (default: 5)
- **`-n, --next_sessions`**: Number of future sessions to display (default: 5)

### Example

```bash
python pet.py -w 25 -b 5 -n 5
```

This command sets a 25-minute work session with a 5-minute break, displaying the next 5 upcoming sessions.

### License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

### Contributions

Feel free to submit issues and pull requests to improve this project!

### Contact

For questions or feedback, please reach out to [emvalbuena@adapting.dev](mailto:emvalbuena@adapting.dev).

