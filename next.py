from sys import argv

log = open("log.txt", "a")

log.write(argv[1] + "\n")
