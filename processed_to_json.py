from functools import total_ordering
import os
import json

all_lines = []

for file_name in os.listdir("edited_scripts"):
    f1_name = os.path.join("edited_scripts", file_name)

    with open(f1_name, "r") as f1:
        text = f1.readline()
        words = text.split()

        total_chars = 0
        current_string = ""
        for (i, word) in enumerate(words):
            if total_chars + len(word) < 2048:
                total_chars += len(word)
                current_string += " " + word
            else:
                curr_line = dict()
                if i < len(words)*0.25: prompt = "Start of "
                elif i < len(words)*0.75: prompt = "Middle of "
                else: prompt = "End of "
                curr_line["prompt"] = prompt + file_name
                curr_line["completion"] = current_string
                total_chars = len(word)
                current_string = word
                all_lines.append(curr_line)

with open("all_data.json", "w") as f2:
    all_lines2 = '\n'.join(json.dumps(rec) for rec in all_lines)
    f2.write(all_lines2)