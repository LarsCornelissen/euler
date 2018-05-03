import os
import sys


def create_file(i):
    os.mkdir(str(i))
    open(str(i) + "/pe_" + str(i) + ".py", 'a').close()
    print("dir: ", i, ", with file: pe_", i, ".py created")


if __name__ == "__main__":
    create_file(int(sys.argv[1]))
