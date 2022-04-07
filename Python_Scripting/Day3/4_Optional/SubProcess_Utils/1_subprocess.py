import subprocess


#subprocess.run('ls -la', shell = True)

#Task 1:
# subprocess.run(['ls', '-la'])  # doesn't capture output
# p1 = subprocess.run(['ls', '-la'])  # doesn't capture output
# print(p1)

# print(p1.args, p1.returncode)
# print(p1.stdout)

#Task 2:
# p1 = subprocess.run(['ls', '-la'], capture_output = True, text = True)  
# print(p1.stdout)

#Task 3:
# p1 = subprocess.run(['ls', '-la'], stdout = subprocess.PIPE, text = True)
# print(p1.stdout)

#Task 4: Re-direct to file
# with open('output.txt','w') as f:
#     p1 = subprocess.run(['ls', '-la'], stdout = f, text = True)

#Task 5: Cmd unsuccessful
# p1 = subprocess.run(['ls', '-la', 'dne'], capture_output = True, text = True)  
# print(p1.returncode, p1.stderr)

#Task 6: Re-direct to stdnull
# p1 = subprocess.run(['ls', '-la','dne'], stderr = subprocess.DEVNULL, text = True)
# print(p1.stderr)

#Task 7: Pipe
# p1 = subprocess.run(['cat', 'test.txt'], capture_output = True, text = True)  
# print(p1.stdout)

# p2 = subprocess.run(['grep', '-n', 'test'], capture_output = True, text = True, input = p1.stdout)  
# print(p2.stdout)

#Task 8: One cmd with shell
p1 = subprocess.run('cat test.txt | grep -n test', capture_output = True, text = True,shell = True)  
print(p1.stdout)
