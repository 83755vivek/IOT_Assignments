#5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
#ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
#Average Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F




def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Enter marks obtained in three subjects:")
    marks1 = float(input("Enter marks of subject 1: "))
    marks2 = float(input("Enter marks of subject 2: "))
    marks3 = float(input("Enter marks of subject 3: "))
    
    average = (marks1 + marks2 + marks3) / 3
    print("Average marks:", average)
    
    grade = calculate_grade(average)
    print("Grade:", grade)

if __name__ == "__main__":
    main()

