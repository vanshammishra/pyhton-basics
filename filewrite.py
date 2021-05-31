# read the file and store the data of that file into the list
# reverse the list

# write back the list into the file

# this would open and close the file,
# r represents that the file is in read mode reader is name of the variable in which we are storing the data
with open('test.txt', 'r') as reader:
    content = reader.readlines() # this would create a list and would store each line separately in it
    # ex. ['a' , 'b' , 'c']
    reversed(content) # reverse the data ['c' , 'b' , 'a']
    # now we need to open that file in write mode which would be represented by w
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
# we have to write a program that can reverse the give number without using the inbuilt
