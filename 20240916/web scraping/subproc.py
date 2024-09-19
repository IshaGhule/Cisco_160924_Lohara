#win programming

import subprocess
# result = subprocess.run(['python','-c','print(2**8)'],shell=True,capture_output=True,text=True)
# print(result.stdout)

result = subprocess.run(['dir'],shell=True,capture_output=True,text=True)
print(result.stdout)