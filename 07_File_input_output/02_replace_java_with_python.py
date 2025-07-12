#Que : WAF that replace all the occurances of "Java" with "Python" in "01_Practice.txt" file

#I/P:

def replace_java_python():

    file_path = "D:/swaro/Documents/Python/07_File_input_output/01_Practice.txt"  # use the actual path

    # Step 1: Read the file content
    with open(file_path,"r") as f:
        data = f.read()

    # Step 2: Replace 'Java' with 'Python'
    new_data = data.replace("Java","Python")
    
    # Step 3: Write the updated content back to the same file
    with open(file_path,"w") as f:
        f.write(new_data)

        
    print("All occurrences of 'Java' have been replaced with 'Python'.")

replace_java_python()
