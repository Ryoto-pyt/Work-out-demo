# Workout Tracker (Beginner Python CLI)

A simple command-line workout tracker for logging and reviewing your exercises, designed for total beginners and anyone wanting to start learning Python!

## Features
- Log workouts: exercise name, number of sets, and weight used.
- View your most recent workout.
- See your workout history for a specific exercise.
- Easy chat-style menu – use words or just numbers!
- No complex setup, no accounts, no advanced tech.

## Requirements
- Python 3 (works great with Python 3.8+, but any Python 3 should do!)

## Installation
1. Download `work out tracker(demo).py` to any folder on your computer.
2. (Optional) Create a fresh folder to keep your workouts organized.

## Usage
Run the script from your command line (Terminal or CMD):
  python work out tracker(demo).py <directory>



You’ll see a menu where you can choose what to do by entering a number (or the command):

- 1 (or log): Log a new workout
- 2 (or last): Show your last workout
- 3 (or history): Show your history for an exercise
- 4 (or help): See the list of commands
- 5 (or exit): Exit the program

Example session:


Choose an option:

1 - Log workout

2 - Show last workout

3 - Show history for an exercise

4 - Help

5 - Exit

Enter command or number: 1

Log workout

Exercise?: Bench Press

Sets?: 3

Weight?: 50

Workout added!


## Data Storage
- All workouts are saved automatically to a file called `workouts.json` in the same folder as your script.
- Your data stays private and local.

## Notes/Limitations
- This project is intentionally simple for learning purposes.
- There’s no password, account, or advanced features.
- Only accepts one user, and does not sync between computers.
