#Task 1:

fin = open('relativity', 'rt' )
poem = fin.read()
fin.close()
print(len(poem))

#Task 2: Read in chunks
# poem = ''
# fin = open('relativity', 'rt' )
# chunk = 100
# while True:
#     fragment = fin.read(chunk)
#     if not fragment:
#         break
#     poem += fragment

# fin.close()
# print(len(poem))

#Task 3: Use readline()
# poem = ''
# fin = open('relativity', 'rt' )
# while True:
#     line = fin.readline()
#     if not line:
#         break
#     #print(line)   # Avoid newlines 
#     poem += line

# fin.close()
# print(len(poem))

#Task 4: Less code than above
# poem = ''
# fin = open('relativity', 'rt' )
# for line in fin:
#     print(line,end='')
#     poem += line
# fin.close()
# print(len(poem))

#Task 5: Use readlines()
# fin = open('relativity', 'rt' )
# lines = fin.readlines()
# fin.close()
# print(len(lines), 'lines read')
# for line in lines:
#     print(line, end='')

#Task 6: Writing Binary data
# bdata = bytes(range(0, 256))
# print(len(bdata))
# print(bdata)
# fout = open('bfile', 'wb')
# fout.write(bdata)
# fout.close()

# fin = open('bfile', 'rb')
# bdata_read = fin.read()
# print(len(bdata_read))
# print(bdata_read)
# fin.close()

# print()

# if bdata == bdata_read:
#     print('Data read correctly')

#Task 7:
# file = open('data.txt')
# for line in file:
#     print(line, end='') # end='' omits the extra newline
# file.close()

#Task 8:
# with open('data.txt') as file:
#     for line in file:
#         print(line, end='') # end='' omits the extra newline

#Task 9:
# with open('data.txt') as file:
#     data = file.read()
# print(data)

#Task 10:
with open('data.txt') as file:
    while (chunk := file.read(10)):
        print(chunk, end='')