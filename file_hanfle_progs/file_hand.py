

# f = open('student.txt', mode = 'w')
# f.write("hello how are you")
# f.close()

'''-------------------------------------------------------------------'''
# text mode and binary mode

# f = open('student.txt', mode = 'w')
# f.write("Hello\n")
# f.write("vaibhav pawar\n")
# f.write("how are you")
# f.close()
# print('finished')


# f = open('student.txt', mode = 'r')
# data = f.read()
# print(data)
# f.close()

# f = open('student.txt', mode = 'rb')
# data = f.read()
# print(data)
# f.close()

'''-----------------------------------------------------------------------'''
# open file

# f = open('student','w')
# f = open('student.txt')
# print(f)

'''-----------------------------------------------------------------------'''
# file object variable

# f = open('student.txt', mode = 'x', encoding = 'utf8' )

# print('file name ;',f.name)
# print('file mode ;',f.mode)
# print('file readable ;',f.readable())
# print('file writable ;',f.writable())
# print('file close ;',f.closed)
# f.close()
# print('file close ;',f.closed)

'''------------------------------------------------------------------------'''
# check file exist or not

# import os
# if os.path.isfile('student.txt'):
#     f = open('student.txt')
#     print('file found')
#     f.close()
    
# else :
#     print('file not')

'''----------------------------------------------------------------------------'''
# writeline method

# f = open('student.txt', mode = 'w')
# st = ['vaibh\n', 'rohit\n', 'dhanu\n']
# f.writelines(st)
# f.close()
# print("successfully")

'''-------------------------------------------------------------------------'''
# readline method
# f = open('student.txt', mode = 'r')
# data1 = f.readline()
# data2 = f.readlines()
# print(data1)
# print(data2)
# f.close()
'''-------------------------------------------------------------------------'''
# second readlines
# f = open('student.txt', mode = 'r')
# data2 = f.readlines()
# for i in data2:
#     print(i,end = '')
# f.close()
'''-------------------------------------------------------------------------'''

# f = open('student.txt', mode = 'w+')
# print(f.tell())
# f.write('youtube')
# print(f.tell())
# f.seek(0)
# data = f.read()
# print(f.tell())
# print(data)
'''-------------------------------------------------------------------------'''
#appending and then reading it wont overwrite existing data

# f = open('student.txt', mode = 'a+')
# print(f.tell())
# f.write('youtube')
# print(f.tell())
# f.seek(0)
# data = f.read()
# print(f.tell())
# print(data)
'''-------------------------------------------------------------------------'''
# copy file content in python

# f1 = open('student.txt', mode = 'r')
# f2 = open('top.txt', mode = 'w')

# data = f1.read()
# f2.write(data)
# f2.close()
# f1.close()
'''-------------------------------------------------------------------------'''
# with statement

# with open('student.txt', mode= 'r') as f:
#     data = f.read()
#     print(data)
#     print(f.close)
# print(f.close)    


