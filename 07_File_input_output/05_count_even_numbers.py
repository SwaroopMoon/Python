#Que : From a file containing numbers separated by commas, print thr count of even numbers.

#I/P :

def find_count():
     
     file_path = r"D:\swaro\Documents\Python\07_File_input_output\numbers.txt"

     with open(file_path,"r") as f:
          data = f.read()
          numbers = data.split(",")
          count = 0
          for num in numbers :
               num = num.strip()
               if num.isdigit() and int(num) %2 == 0 :
                    count+=1
          print(count)

find_count()