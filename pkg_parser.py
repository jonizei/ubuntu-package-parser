
def parse(filename):
    file = open(filename, "r")
    lines = file.readlines()

    for i in range(10):
        print(lines[i])