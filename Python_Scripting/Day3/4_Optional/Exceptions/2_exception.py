# int(input("Enter an integer: "))

# # try:
# #     number = int(input("Enter an integer: "))
# # except ValueError:
# #     print("That was not an integer")

# print('Hello World')








# def divide(num1, num2):
#     try:
#         print(num1 / num2)
#     except (TypeError, ZeroDivisionError):
#         print("encountered a problem")

# divide(20.0, 'hi')


def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError as err:
        print('Both arguments must be numbers')
        print(err)
    except ZeroDivisionError as err:
        print('num2 must not be 0')
        print(err)

divide(20. , 0 )  # (20.0,10), (20. , 0) , (20, 'hi')