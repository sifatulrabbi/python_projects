import os

dir_path = f"{os.getcwd()}/read_write_files/files"


file1 = open(f"{dir_path}/file1.txt", "r")
file2 = open(f"{dir_path}/file2.js", "r")
file3 = open(f"{dir_path}/file3.xml", "r")

os.system(f"sudo rm -rf {dir_path}/file1.txt")
os.system(f"sudo echo '{file3.read()}' >> {dir_path}/file1.xml")

print(file1.read())
