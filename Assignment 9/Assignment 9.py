old_file = open("oldfile.txt", "r")

lines = old_file.readlines()

old_file.close()

lines.reverse()

new_file = open("newfile.txt", "w")

for line in lines:
    new_file.write(line)

new_file.close()
