#str_3.py
#Demonstrates the string indexing, slicing, striding functionalities

s2 = 'The waxwork man'

#Construct the string 'The waxwork woman'

#Return the string 'The waxwork woman' from the string s2
s3 = s2[0:12] + 'wo' + s2[12:]
#Use -ve index to extract the substring
s4 = s2[0:4] + s2[4:12] + 'wo' + s2[-3:] 


print('s2 =', s2, '\t', 's3 =', s3)
if s3 == s4:
    print('s3 & s4 are the same')
else:
    print('You have done a mistake!!! Please check')
    print(f's3: {s3} s4:{s4}')
    #print('s3:', s3)
    



