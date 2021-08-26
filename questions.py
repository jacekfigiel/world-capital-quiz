from capitals_list import capitals
import random

with open("test.txt", "w") as text:
    for country in list(capitals.keys()):
        text.write("What city is a capital of " + country + "?")
        correct_answer = capitals.get(country)
        wrong_answer_list = list(capitals.values())
        wrong_answers = random.sample(wrong_answer_list, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        for question in range(4):
            text.write("\n" + "ABCD"[question] + ". " + str(answer_options[question] + "\n"))
        text.write("\n")

