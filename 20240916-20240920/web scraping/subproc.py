#win programming

import subprocess
# result = subprocess.run(['python','-c','print(2**8)'],shell=True,capture_output=True,text=True)
# print(result.stdout)

result = subprocess.run(['dir'],shell=True,capture_output=True,text=True)
print(result.stdout)

#OS based commands:
import os
os.system('dir')
os.popen('dir').read()
cwd =os.getcwd()
print("Current working directory: ", cwd)
os.listdir()
os.getcwd()
#'C:\\Mywork\\Source\\Cisco_160924_Lohara'
os.mkdir('new_dir')
os.listdir()
