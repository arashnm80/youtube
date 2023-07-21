from collections import namedtuple

N = int(input())
columns = input().split()
Student = namedtuple("Student", columns)
my_table = []
for i in range(N):
    line = input().split()
    my_table.append(Student(*line))
    
total = 0
for s in my_table:
    total += int(s.MARKS)
    
print(total / N)
