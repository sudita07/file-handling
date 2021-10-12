# the below program is for reading a file
# d=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/data.txt","r")
# print(d.read())
# print(d.readline())
# print(d.readline())


# write a program to write on a file
# f=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/data.txt","r")
# f1=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/abc.txt","w")
# f1.write("i dont like school")
# f1.write("i dont want to go to school")


# write a program to append on a file
# f=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/data.txt","r")
# f1=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/abc.txt","a")
# f1.write("mobile")


# write a program to read all the text from data.txt
f=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/data.txt","r")
f1=open("C:/Users/CHAWLA/PycharmProjects/pythonProject/class 9/abc.txt","w")
for data in f:
    f1.write(data)
f1.write("i dont like school")
f1.write("i dont want to go to school")
f1.write("mobile")