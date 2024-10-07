# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

# Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

import random

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

emotions = ["Happy", "Sad", "Energetic", "Calm"]
week_days_index = range(len(days_of_the_week))
for day in week_days_index:
    mood_on_day = random.choice(emotions)
    print(f"On {days_of_the_week[day]} I felt {mood_on_day} !")