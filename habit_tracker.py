from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")

file = open("ferguson_tracker_log.txt", "a")

print("\n🧭 Ferguson Daily Tracking Sheet\n")

file.write(f"\n===== {date} =====\n")

# MORNING FOUNDATION
wake = input("Wake-up time: ")
sleep = input("Sleep hours: ")
stretch = input("Stretch / mobility (Y/N): ")
meditation = input("Meditation 30 min (Y/N): ")
exercise = input("Walk / exercise (Y/N): ")
mindset = input("Mindset on waking (Calm / Restless / Focused / Low energy): ")

file.write(f"\nMorning Foundation\nWake:{wake} Sleep:{sleep} Stretch:{stretch} Meditation:{meditation} Exercise:{exercise} Mindset:{mindset}\n")

# PHYSICAL DISCIPLINE
exercise_type = input("\nExercise type + minutes: ")
steps = input("Steps: ")
water = input("Water intake (L): ")
junk = input("Junk / fried snacks avoided (Y/N): ")
night_food = input("Night food discipline maintained (Y/N): ")
last_meal = input("Last meal time: ")

file.write(f"\nPhysical Discipline\nExercise:{exercise_type} Steps:{steps} Water:{water} Junk avoided:{junk} Night food:{night_food} Last meal:{last_meal}\n")

# WORK
checkin = input("\nOffice check-in time: ")
primary_task = input("Primary task planned: ")
task_done = input("Primary task completed (Y/N): ")
impact_action = input("One high-impact action today: ")

file.write(f"\nWork\nCheck-in:{checkin} Task:{primary_task} Completed:{task_done} Impact:{impact_action}\n")

# EMOTIONAL CONTROL
trigger = input("\nEmotional trigger noticed (Y/N): ")
manipulation = input("Manipulation resisted (Y/N): ")
boundary = input("Boundary enforced (Y/N): ")
manager = input("Manager interaction calm (Y/N/NA): ")

file.write(f"\nEmotional Control\nTrigger:{trigger} Manipulation resisted:{manipulation} Boundary:{boundary} Manager calm:{manager}\n")

# ATTITUDE
attitude = input("\nAttitude maintained (Y/N): ")
calm_pressure = input("Spoke calmly under pressure (Y/N): ")
no_reaction = input("No emotional reaction (Y/N): ")

file.write(f"\nAttitude\nAttitude maintained:{attitude} Calm pressure:{calm_pressure} No reaction:{no_reaction}\n")

# MINDFUL CONTROL
sexual_control = input("\nSexual control maintained (Y/N): ")
impulse_control = input("Impulse control maintained (Y/N): ")
urge_redirect = input("Urge redirected (Y/N): ")

file.write(f"\nMindful Control\nSexual control:{sexual_control} Impulse control:{impulse_control} Urge redirected:{urge_redirect}\n")

# LEARNING
lesson = input("\nOne lesson today: ")
correction = input("What to correct tomorrow: ")

file.write(f"\nLearning\nLesson:{lesson}\nCorrection tomorrow:{correction}\n")

# FINAL SCORES
discipline = input("\nDiscipline score (0-10): ")
emotion = input("Emotional control score (0-10): ")
leadership = input("Leadership presence score (0-10): ")
energy = input("Energy score (0-10): ")

file.write(f"\nScores\nDiscipline:{discipline} Emotion:{emotion} Leadership:{leadership} Energy:{energy}\n")

file.write("\n==============================\n")

file.close()

print("\n✅ Daily record saved successfully!\n")