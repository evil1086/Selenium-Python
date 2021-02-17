# file = open('text.txt')


# print all the content of the file
# print(file.read())

# it will read 5 character from the file - It consider next line as single character
# print(file.read(5)

# print first line of the file
# print(file.readline())

# print whole file using readline method

'''
def reader():
    line = file.readline()
    while line != '':
        print(line)
        line = file.readline()


# write in the file and reverse it
with open('text.txt', 'r') as reader:
    # initial reader 1st line
    content = reader.readlines()
    print(content)
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

num = 0

assert(num == 1)
if num != 1:
    raise Exception("Number is greater than 0")
'''


try:
    with open('text.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('cleaning up task is completed')



