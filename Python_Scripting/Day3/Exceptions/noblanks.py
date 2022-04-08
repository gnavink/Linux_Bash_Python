##Reads in text files construct a list lines.
filename = '1.png' #'data.txt' #'nodata.txt' , '1.png'


  
def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if ( line:= line.strip()):   #What happens if its changed to if (line.strip()):
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines

try:
    lines = read_data(filename)
except UnicodeDecodeError as err: 
    print('UnicodeDecodeError has happened' )
else:
    print('No exceptions in top level code')
finally:
    print('Cleaning up happens in top level')

#print(lines)

##What happens if I pass an image file as input??