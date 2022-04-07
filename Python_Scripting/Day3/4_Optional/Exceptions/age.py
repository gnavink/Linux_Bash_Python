#age.py
# This program keeps prompting the user to enter a valid age.
# If a valid integer is enter, it prints and exits the function

# def get_int(msg):
#     while(True):
#         i = int(input(msg))
#         print()
#         return i



# def get_int(msg):
#      while(True):
#         try:
#             i = int(input(msg))
#             print()
#             return i
#         except ValueError as err:
#             print(err)
        

# while(cond):
#     body1
# else:
#     bodyelse

# try:
#     tryblock
# except  1:
#     exceptblock1
# except 2:
#     except2
# else:
#     elseblock
# finally:


def get_int(msg):
     while(True):
        try:
            i = int(input(msg))
            print()            
        except ValueError as err:
            print(err)
        else:
            print('I didn\'t find exceptions in my code')
            return i
        finally:
            print('''I am cleaning up my code. For eg freeing up resources like filehandlers,sockets''')    

age = get_int('Enter your age:')
print(f'age = {age}')
