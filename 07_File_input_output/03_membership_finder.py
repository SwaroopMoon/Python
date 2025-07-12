#Que: Search if word "learning" exists in "01_Practice.txt" or not

#I/P:

def exists_or_not():

    file_path = r"D:\swaro\Documents\Python\07_File_input_output\01_Practice.txt"   #using r"directory" to treat path as raw string

    with open(file_path,"r") as f:
        data = f.read()

        if "learning" in data :
            print("It exists in the file")
        else:
            print("It does not exist in the file")

exists_or_not()