# Add Student
def add_student(students):
    # print('I\'m in add_student() function')
    roll_num = input('Enter roll number : ')
    if roll_num in students:
        print('Student roll number is already exist...')
        return
    name = input('Enter student name : ').capitalize()
    students[roll_num] = {'name':name,'attendance':[]}
    print(f'\nStudent {name} is added successfully...')

# Remove Student
def remove_student(students):
    # print('I\'m in remove block')
    roll_num = input('Enter the roll number to remove : ')
    if roll_num in students:
        del(students[roll_num])
        print(f'Student with {roll_num} removed successfully...')
    else:
        print(f'Student with {roll_num} is not in data base...')

# For Mark Attendence
def mark_attendence(students):
    # print('In mark_attendance block')
    if len(students) == 0:
        print('No student is there...')
        return
    for roll_num , details in students.items():
        status = input(f'Mark attendance for {details['name']} (Roll no : {roll_num} [P/A]) : ').strip().upper()
        if status in ('P','A'):
            if status == 'P':
                details['attendance'].append('P')
            else:
                details['attendance'].append('A')

# For Mark Each Student Attendence
def mark_each_student_attendence(students):
    # print('In mark_attendance block')
    if len(students) == 0:
        print('No student is there...')
        return
    num = input('Enter your roll no. : ')
    for roll_num , details in students.items():
        if roll_num == num:
            status = input(f'Mark attendance for {details['name']} (Roll no : {roll_num} [P/A]) : ').strip().upper()
            if status in ('P','A'):
                if status == 'P':
                    details['attendance'].append('P')
                else:
                    details['attendance'].append('A')
        else: print(f'Student with roll no. : {num} not found...')
          
                
# Attendence Details->
def attendance_details(students):
    # print('in Attendance details block')
    if not students:
        print('No student to display....')
        return
    print('\n...Attendance details...')
    # for roll_num, detais in students.items():
    #     # print(f'Roll no. : {roll_num}, Name : {detais['name']}, Attendance : {detais['attendance']}')
    #     print(f'Roll no. : {roll_num}, Name : {detais['name']}, Attendance : {', '.join(detais['attendance'])}')
    #     # print(f'Roll no. : {roll_num}, Name : {detais['name']}, Attendance : {(detais['attendance'])}')

    attendance_percentage(students) #Instead of above code use this line


# Attendance %
def attendance_percentage(students):
    # print('In attendance percent block')
    if not students:
        print('no student attendance percent to display...')
        return
    for roll_num, details in students.items():
        percent,present, absent, total = 0, 0, 0, 0
        

        if len(details['attendance']) == 0:
            print(f'\nNo attendance recorded yet for {details['name']}...')
        else:
            for attendance in details['attendance']:
                total+=1
                if attendance == 'P':
                    present+=1
                if attendance == 'A':
                    absent+=1
                
        if total is not 0:   
            percent = (present/total)*100
        print(f'Roll no. : {roll_num} Student : {details['name']} Attendance precentage : {percent}%')
        
# Each Student Details
def each_student_details(students):
    # print('In each student detail block')
    num = input('Enter roll number of student : ')       
    if not num in students:
        print(f'Student with roll number : {num} is not in our data base...')
        return
    for roll_num, details in students.items():
        if roll_num == num:
            print(f'Roll no. : {roll_num}, Name : {details['name']}, Attendance : {', '.join(details['attendance'])}')
        
# Each Student Percenatge
def each_student_percentage(students):
    # print('each_student_percentage')
    num = input('Enter roll number of student : ')
    if not num in students:
        print(f'Student with roll number : {num} is not in our data base...')
        return
    
    for roll_num, details in students.items():
        
        if roll_num == num and len(details['attendance']) != 0:
            total,present, absent, total = 0, 0, 0, 0
            for attendance in details['attendance']:
                total+=1
                if attendance == 'P':
                    present+=1
                if attendance == 'A':
                    absent+=1
            percent = (present/total)*100
            print(f'Roll no. : {roll_num} Student : {details['name']} Attendanc precentage : {percent}%')

# Attendance Summary
def attendance_summary(students):
    if not students:
        print('No student is there. Add first..')
        return
    for roll_num,details in students.items():
        print(f'Roll no. : {roll_num}, Name : {details['name']} Attendance : {', '.join(details['attendance'])} ')
    

# Main()-->>
students = {}
while True:
    print('\n...Attendance Management System...')
    print('1. Adddd student')
    print('2. Remove student')
    print('3. Mark attendence')
    print('4. Mark each student attendence')
    print('5. View attendance Details')
    print('6. View attendance details for each')
    
    print('7. Attendance percentage')
    print('8. Attendance percentage for each')
    print('9. Get attendance summary.')
    print('10. For Exit / Terminate')

    choice = input('Enter the number according to ur choice : ')
    if choice == '1':
        print("\n")
        add_student(students)
    elif choice == '2':
        print("\n")
        remove_student(students)
    elif choice == '3':
        print("\n")
        mark_attendence(students)
    elif choice == '4':
        print("\n")
        mark_each_student_attendence(students)
    elif choice == '5':
        print("\n")
        attendance_details(students)
    elif choice == '6':
        print("\n")
        each_student_details(students)
    elif choice == '7':
        print("\n")
        attendance_percentage(students)
    elif choice == '8':
        print("\n")
        each_student_percentage(students)
    elif choice == '9':
        print("\n")
        attendance_summary(students)
    elif choice == '10':
        print('Completed')
        break
    else:
        print("Invalid Input 😒")
    