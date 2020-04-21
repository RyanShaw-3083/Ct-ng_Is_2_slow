#!/usr/bin/env python
import os

if __name__ == "__main__":
    repo = input("Input new mirror: ")
    packages = os.listdir("./packages")
    for p in packages:
        try:
            targetfd = open("./packages/" + p + "/package.desc.new", 'w')  # Close +17

            originfd = open("./packages/" + p + "/package.desc", 'r')
            data = originfd.readlines()
            originfd.close()

            newfile = []

            for line in data:
                m = line.replace('mirrors=', "### mirrors=")
                r = line.replace("repository=", "### repository=")
                if m != line:
                    line = m
                elif r != line:
                    line = r
                targetfd.write(line)
            targetfd.write("mirrors=" + repo + '\n')
            targetfd.close()

            os.remove("./packages/" + p + "/package.desc")
            os.rename("./packages/" + p + "/package.desc.new", "./packages/" + p + "/package.desc")
        except NotADirectoryError:
            pass
