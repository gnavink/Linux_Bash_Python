# str_5.py
#Demonstrates : Functions

s4 = 'Sarala*1950-12-25*2011-11-20'

def split_fields(record) :
    fields = record.split('*')
    print(fields)
    B_day = fields[1].split('-')
    D_day = fields[2].split('-')
    num_yrs_lived = int(D_day[0]) - int(B_day[0])
    return num_yrs_lived

   
num_yrs_lived = split_fields(s4)
print(f'Sarala lived for {num_yrs_lived} years')


