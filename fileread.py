trf = open('test.txt')
print(trf.read()) # read all the contents of the file
print(trf.read(5)) # by passing the arguments inside the read() we can read the number of characters that we have
# passed in the read().



# to read one single line at a time use readline()

print(trf.readline())
# print line by line by using the readline()
line = trf.raedline()
while line!="":
    print(line)
    line = trf.readline()


# readlines() is also a method that is  used to read the content of the file but at the same time it also creates the
# creates the list and stoores each line in it seperately

trf.close()