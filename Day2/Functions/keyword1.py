def add_person_details(ssn, surname, **kwargs): #kwags = {'age': 45, 'forename':'Navin'}
    print("SSN =", ssn)
    print("surname =", surname)
    for key in kwargs: #sorted(kwargs)    
        print(f'{key}, {kwargs[key]}')
        #print("{0} = {1}".format(key, kwargs[key]))

#add_person_details(83272171, 'Kumar', forename='Navin', age=45)
add_person_details(83272171, 'Kumar',age=45, forename='Navin' ) #dict.keys() = 'forename', 'age'
