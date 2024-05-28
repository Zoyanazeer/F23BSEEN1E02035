class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def read_employee_data():
    employees = []
    print("Enter employee data (type 'done' to finish):")
    
    while True:
        name = input("Enter employee name: ")
        if name.lower() == 'done':
            break
        salary = float(input(f"Enter salary for {name}: "))
        employees.append(Employee(name, salary))
    
    return employees

def calculate_salary_statistics(employees):
    total_salary = sum(e.salary for e in employees)
    average_salary = total_salary / len(employees) if employees else 0
    min_salary = min(e.salary for e in employees) if employees else 0
    max_salary = max(e.salary for e in employees) if employees else 0
    
    return total_salary, average_salary, min_salary, max_salary

def display_salary_report(employees):
    total_salary, average_salary, min_salary, max_salary = calculate_salary_statistics(employees)
    
    print("\nSalary Report")
    print("-------------")
    print(f"Total Salary: ${total_salary:,.2f}")
    print(f"Average Salary: ${average_salary:,.2f}")
    print(f"Minimum Salary: ${min_salary:,.2f}")
    print(f"Maximum Salary: ${max_salary:,.2f}")
    
    print("\nDetailed Employee Salaries:")
    for e in employees:
        print(f"{e.name}: ${e.salary:,.2f}")

def main():
    employees = read_employee_data()
    display_salary_report(employees)

if __name__ == "__main__":
    main()