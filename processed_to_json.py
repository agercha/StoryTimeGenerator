from functools import total_ordering
import os
import json

all_lines = []
all_intros = []

for file_name in os.listdir("edited_scripts"):
    f1_name = os.path.join("edited_scripts", file_name)

    with open(f1_name, "r") as f1:
        text = f1.readline()
        words = text.split()

        total_chars = 0
        current_string = ""
        first = True
        for (i, word) in enumerate(words):
            if total_chars + len(word) < 2048:
                total_chars += len(word)
                current_string += " " + word
            else:
                curr_line = dict()
                if i < len(words)*0.25: prompt = "Start of "
                elif i < len(words)*0.75: prompt = "Middle of "
                else: prompt = "End of "
                curr_line["prompt"] = prompt + (file_name).strip(".txt")
                curr_line["completion"] = current_string
                all_lines.append(curr_line)
                if first:
                    first = False
                    curr_intro = dict()
                    curr_intro["prompt"] =  (file_name).strip(".txt")
                    curr_intro["completion"] = current_string
                    all_intros.append(curr_intro)

                total_chars = len(word)
                current_string = word
                all_lines.append(curr_line)

with open("all_data.json", "w") as f2:
    all_lines2 = '\n'.join(json.dumps(rec) for rec in all_lines)
    f2.write(all_lines2)

with open("all_intros.json", "w") as f3:
    all_intros2 = '\n'.join(json.dumps(rec) for rec in all_intros)
    f3.write(all_intros2)
