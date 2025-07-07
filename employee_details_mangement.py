import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5028",
    database="emp"
)
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(10),
    email VARCHAR(100) UNIQUE,
    position VARCHAR(50),
    login_username VARCHAR(50) UNIQUE
)
""")
con.commit()

def add_employee():
    print("\n Add New Employee")
    emp_id = int(input("Enter Employee ID: "))
    first = input("Enter First Name: ")
    last = input("Enter last name: ")
    email = input("Enter Email: ")
    position = input("Enter Position: ")
    login = input("Enter Login Username: ")

    query = "INSERT INTO employee (emp_id, first_name, phone_number, email, position, login_username) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (emp_id, first, last, email, position, login)

    try:
        cursor.execute(query, values)
        con.commit()
        print(" Employee added successfully.")
    except mysql.connector.Error as e:
        print(" Error:", e)


def show_employees():
    print("\n All Employees")
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_employee():
    print("\n Update Employee Position")
    emp_id = int(input("Enter Employee ID: "))
    new_position = input("Enter new position: ")
    new_email = input("Enter new email: ")


    try:
        cursor.execute("UPDATE employee SET position = %s WHERE emp_id = %s", (new_position, emp_id))
        con.commit()
        print(" Employee updated.")
    except mysql.connector.Error as e:
        print(" Error:", e)


def delete_employee():
    print("\n Delete Employee")
    print("1.Enter Employee ID to delete: ")
    print("2. Enter new email to delete:")
    print("3. Enter new name to delete:")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        cursor.execute("DELETE FROM employee WHERE emp_id = %s", (emp_id,))
        con.commit()
        print("Employee deleted." + emp_id)
    elif choice == '2':
        email = input("Enter Employee MailID: ")
        cursor.execute("DELETE FROM employee WHERE email = %s", (email,))
        con.commit()
        print("Employee deleted." + email)
    elif choice == '3':
        first_name = input("Enter Employee NAME: ")
        cursor.execute("DELETE FROM employee WHERE first_name = %s", (first_name,))
        con.commit()
        print("Employee deleted." + first_name)

    else:
        print(" Invalid choice.")
        return

    result = cursor.fetchone()

    if result:

        print(" Employee Found:\n", result)

    else:

        print("No employee found with the given detail.")

def view_employee():
    print("\n Search Employee")
    print("1. Search by Employee ID")
    print("2. Search by Email")
    print("3. Search by Login Username")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        cursor.execute("SELECT * FROM employee WHERE emp_id = %s", (emp_id,))
    elif choice == '2':
        email = input("Enter Email: ")
        cursor.execute("SELECT * FROM employee WHERE email = %s", (email,))
    elif choice == '3':
        login = input("Enter Login Username: ")
        cursor.execute("SELECT * FROM employee WHERE login_username = %s", (login,))
    else:
        print(" Invalid choice.")
        return

    result = cursor.fetchone()
    if result:
        print(" Employee Found:\n", result)
    else:
        print("No employee found with the given detail.")


def menu():
    while True:
        print("\n=== ADMIN SHOW MENU ===")
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. View Particular Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            show_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice =='5':
            view_employee()
        elif choice == '6':
            print("thankyou for login !")
            break
        else:
            print(" Invalid choice. Try again.")


menu()
cursor.close()
con.close()
