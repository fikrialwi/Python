import os
import glob

# print(os.listdir("E:\My Library\My Book"))
os.chdir("E:\My Library\My Book")
for i in glob.glob("*.epub"):
    print(i)

    