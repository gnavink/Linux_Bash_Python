# average.py
# Computes the average of a list of numbers

def avg(inlist:list) -> float :
    "Returns the average of a list of integers. "
    lenlist = len(inlist)
    return sum(inlist) / lenlist

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    average = avg(a)
    print(f'Average of list {a}  is : {average}')