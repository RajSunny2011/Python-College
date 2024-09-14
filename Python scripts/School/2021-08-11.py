#q: WAP to create student.dat with the following data- Student Name, Addmision number, Percentage
import pickle as pk
n = int(input('Enter the number of students: '))
List = []
for i in range(n):
    L = []
    a = input('Enter name: ')
    L.append(a)
    a = input('Enter addmission number: ')
    L.append(a)
    a = input('Enter percentage: ')
    L.append(a)
    List.append(L)
student = open('student.dat','wb+')
pk.dump(List,student)
student.seek(0)
k = pk.load(student)
print(k)
student.close()