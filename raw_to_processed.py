import os

def rem_junk(s):
    while "\n" in s: s = s.replace("\n", "")
    while ":" in s: s = s.replace(":", "")
    for i in range(10):
        while (str(i)) in s: s = s.replace(str(i), "")
    return s

for file_name in os.listdir("raw_scripts"):
    f1_name = os.path.join("raw_scripts", file_name)

    with open(f1_name) as f1:
        lines = f1.readlines()
        newlines = [rem_junk(l) for l in lines]

    with open("edited_scripts/" + file_name, "w") as f2:
        f2.write(" ".join(newlines))