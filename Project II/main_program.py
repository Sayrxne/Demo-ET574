#Project II - Chasyl De Guzman

def main():
    # Step 1: Prompt for the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

              # Step 2: Collect grades
    grades = []
    for i in range(num_students):
        while True:
            try:
                grade = float(input(f"Enter grade for student {i+1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Step 3: Calculate average
    average = sum(grades) / len(grades)
    print(f"The average grade for {num_students} students is: {average:.2f}")

# Run the main function
if __name__ == "__main__":
    main()