file_read = open("pop2.txt", "r")

data = file_read.read().split("\n")

n = 11
x = 0
while True:
    try:
        del data[(n - 1) + (x * 11) :: n]
        del data[(n - 2) + (x * 11) :: n]
        del data[(n - 3) + (x * 11) :: n]
        del data[(n - 4) + (x * 11) :: n]
        del data[(n - 5) + (x * 11) :: n]
        del data[(n - 7) + (x * 11) :: n]
        del data[(n - 8) + (x * 11) :: n]
        del data[(n - 9) + (x * 11) :: n]
        del data[(n - 11) + (x * 11) :: n]
        x = x + 1
    except:
        break

file2 = open("data.txt", "w")

for x in data:
    file2.write(x + "\n")
