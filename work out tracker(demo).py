import json
import datetime

# File to store workouts
FILE = 'workouts.json' 

print("Welcome to your workout tracker")

# Try to read existing workouts from the file
try:
    with open(FILE, 'r') as f:
        workouts = json.load(f)
except:
    workouts = []

while True:
    print("\nChoose an option:")
    print("1 - Log workout")
    print("2 - Show last workout")
    print("3 - Show history for an exercise")
    print("4 - Help")
    print("5 - Exit")
    user_input = input("Enter command or number: ").lower()

    if user_input in ["log","1"]:
        # Get workout details from user
        exercise = input("Name of the Exercise?: ")
        sets = input("no of Sets?: ")
        weight = int(input("your Weight?: "))
        
        # Create new workout
        new_workout = {'date': str(datetime.datetime.now()),
            'exercise': exercise,
            'sets': sets,
            'weight': weight }
        # Add workout to list
        workouts.append(new_workout)
        # Save to file
        with open(FILE, 'w') as f:
            json.dump(workouts, f)
        print("Workout added!")

    elif user_input in ["Last","2"]:
        # Show last workout
        if len(workouts) == 0:
            print("No workouts recorded yet.")
        else:
            w = workouts[-1]
            print("Last workout:")
            print(f"Exercise: {w['exercise']}\nSets: {w['sets']}\nWeight: {w['weight']}\nDate: {w['date']}")

    elif user_input in ["history","3"]:
        ex = input("Which exercise? ")
        found = False
        for w in workouts:
            if w['exercise'].lower() == ex.lower():
                print(f"\nExercise: {w['exercise']}\nSets: {w['sets']}\nWeight: {w['weight']}\nDate: {w['date']}","\n")
                found = True
        if not found:
            print("No recorded workouts for that exercise.")

    elif user_input in ["help","4"]:
        print("Help")
        print("\nCommands:")
        print("1 or log     - Log a workout")
        print("2 or last    - Show last workout")
        print("3 or history - Show history for an exercise")
        print("4 or help    - Show this help message")
        print("5 or exit    - Exit the program")

    elif user_input in ["exit","5"]:
        print("      \nBye! \n Work Hard Or Regret")
        break

    else:
        print("Unknown command. Type 'help' or Enter '4' for commands.")

