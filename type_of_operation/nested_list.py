'''
if __name__ == '__main__':
    marksheet = []
    second_lowest_grade = []
    sname = []
    student_number = int(input())
    for _ in range(0, student_number):
        student_name = input()
        grade = float(input())
        marksheet.append([student_name, grade])
    # marksheet done
    print(marksheet)

    # order
    order = sorted(marksheet, key=lambda x: int(x[1]))
    print("order", order)
    for i in range(student_number):
        if (order[i][1] != order[0][1]):
            second_lowest_grade.append(order[i][1])

    # print second lowest grade
    print(second_lowest_grade)

    sname = [x[0] for x in order if x[1] == second_lowest_grade]
    sname.sort()

    for s_name in sname:
        print(s_name)
'''

marksheet = []
second_lowest_names = []
scores = set()
student_number = int(input())

for _ in range(student_number):
    student_name = input()
    grade = float(input())
    marksheet.append([student_name, grade])
    scores.add(grade)
        
second_lowest_grade = sorted(scores)[1]

for student_name, score in marksheet:
    if score == second_lowest_grade:
        second_lowest_names.append(student_name)

for student_name in sorted(second_lowest_names):
    print(student_name, end='\n')