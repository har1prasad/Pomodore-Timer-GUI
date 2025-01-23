# Pomodoro Timer GUI

This project is a **Pomodoro Timer** application built using Python and the Tkinter library. The Pomodoro Timer is designed to help you stay focused and productive by following the Pomodoro Technique—breaking work into intervals separated by short breaks.

## Features

1. **Work Sessions and Breaks**
   - Work sessions are set to 1 minute (configurable via constants).
   - Short breaks are set to 1 minute.
   - After four work sessions, a long break of 20 minutes is triggered.

2. **User-Friendly Interface**
   - A visual timer with a countdown.
   - Labels indicating whether it's time to "Work!" or "Break."

3. **Progress Tracking**
   - Displays a checkmark (✅) for each completed work session.

4. **Start and Reset Buttons**
   - Start the timer with the "Start" button.
   - Reset the timer and progress with the "Reset" button.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- Tkinter library (comes pre-installed with Python on most systems).
- A `tomato.png` image file for the timer interface.

### How to Run
1. Clone or download the repository.
2. Place the `tomato.png` file in the same directory as the script.
3. Run the script:
   ```bash
   python pomodoro_timer.py
   ```
4. The Pomodoro Timer GUI will open.

## File Structure

- **pomodoro_timer.py**: The main Python script containing the application logic.
- **tomato.png**: An image file used for the timer visualization.

## How It Works

1. **Start the Timer**
   - Click the "Start" button to begin the first work session.
   - The timer will automatically switch between work and break sessions.

2. **Progress Indicators**
   - For every completed work session, a checkmark (✅) will appear below the timer.

3. **Reset the Timer**
   - Click the "Reset" button to stop the timer and clear all progress.

## Customization

You can modify the following constants in the script to customize the timer settings:

- `WORK_MIN`: Duration of a work session (in minutes).
- `SHORT_BREAK_MIN`: Duration of a short break (in minutes).
- `LONG_BREAK_MIN`: Duration of a long break (in minutes).
