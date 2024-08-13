import sys, subprocess


if len(sys.argv) != 2:
    print("ERROR")
    exit(0)

resp = subprocess.getoutput(f"man {sys.argv[1]} | cat")

lines = resp.split("\n")
ignore = True
data = ""
for line in lines:
    if line.strip() == "DESCRIPTION":
        break

    if line.strip() == "SYNOPSIS":
        ignore = False
        continue;

    if ignore == False:
        data += f"{line}\n"

print(data)