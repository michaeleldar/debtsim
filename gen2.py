file_read = open("pop2.txt", "r")

data = file_read.read().split("\n")

n = 11
x = 1
for x in range(0, 100):
    try:
        del data[(n - 1) + x :: n]
        del data[(n - 2) + x :: n]
        del data[(n - 3) + x :: n]
        del data[(n - 4) + x :: n]
        del data[(n - 5) + x :: n]
        del data[(n - 7) + x :: n]
        del data[(n - 8) + x :: n]
        del data[(n - 9) + x :: n]
        del data[(n - 11) + x :: n]
        x = x + 10
    except:
        break

file2 = open("data.txt", "w")

for x in data:
    file2.write(x + "\n")
