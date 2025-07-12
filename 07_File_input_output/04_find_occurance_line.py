#Que : Write a function in which line of the file does the word "learning" occur first in the "01_Practice.txt"
#Print "-1" if word not found.

# I/P:

def occurance_line():

    file_path = r"D:\swaro\Documents\Python\07_File_input_output\01_Practice.txt"

    with open(file_path, "r") as f:
        for number,line in enumerate(f, start=1):
            if "learning" in line:
                print(number)
                return
        print(-1)

occurance_line()