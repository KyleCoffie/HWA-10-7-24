
# 2. Double Scoop with Nested Loops
# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"


import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday ", "Sunday "]
times = ["morning", "afternoon", "evening"]
for day in days:
    for time in times:
        mood = random.choice(moods)
        print("On " + day  + time + " I was feeling " + mood)