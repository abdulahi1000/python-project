# try exception handling 
# 1. FileNotFoundError


# raised when a file or directory is requested but doesn’t exist.
# Example
try:
 file_name = 'myfile.txt'
 with open(file_name) as f:
     print(f)
except:
    print("File Not Found")




# 2. Exception FileExistsError


# Raised when trying to create a file or directory which already exists.
# Example:
import os
try:
 file_name = 'myfile.txt'
 
 os.mkdir('./myfile.txt')
except FileExistsError:
 print("File Exists Error")


choose = input('Rewrite y/n')


# 3. PermissionError
# Raised when trying to run an operation without the adequate access rights 
# Example
import os
try:
 os.mkdir('admin_data', 000)
 with open('admin_data') as f:
    print(f)
except PermissionError:
    print("Access denied")


# Describe how you might deal with each error if you were writing a large production program. 
# To deal with error when writting a large program, i will make sure to test the project to ses
# the kind of error it's bringing out then write a try-exception block for it.