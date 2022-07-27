class Employers:

    def __init__(self):
        self.employers_count = 0
        self.employers_database = dict()

    def show_employers(self):
        print(self.employers_database)

    def add_employer(self, first_name, last_name, age, job, salary, bonus):

        try:
            salary = int(salary)
            bonus = int(bonus)

        except ValueError:
            print("Bonus or salary is not a number!")
            return 0

        self.employers_database[self.employers_count] = [first_name, last_name, age, job, salary, bonus, salary + bonus]
        self.employers_count += 1

        print("Employer added successfully!")

    def remove_employer(self, first_name, last_name):
        for item in self.employers_database:
            if self.employers_database[item][0] == first_name and self.employers_database[item][1] == last_name:
                del self.employers_database[item]
                print("Successfuly removed employer!")
                return 0

        print("No such user to delete!")

    def apply_bonus(self, first_name, last_name, bonus):

        try:
            bonus = int(bonus)
        except ValueError:
            print("Bonus is not a number!")
            return 0

        for key, val in self.employers_database.items():
            if val[0] == first_name and val[1] == last_name:
                self.employers_database[key][5] += bonus

                self.employers_database[key][6] = self.employers_database[key][4] + self.employers_database[key][5]

                print("Successfully applied bonus: ", bonus)
                print(self.employers_database[key])
                return 0

        print("There is no such employer in database!")

    def add_bonus_to_entire_department_employers(self, department_name, bonus_value, departments_database):
        try:
            bonus_value = int(bonus_value)
            for employer in departments_database[department_name]:
                if employer in self.employers_database:
                    self.employers_database[employer][5] += bonus_value
                    self.employers_database[employer][6] = self.employers_database[employer][4] + \
                                                           self.employers_database[employer][5]

            print(f'Successfully added bonus to department: {department_name}')

        except KeyError:
            print(f'No such department: {department_name}!')

        except ValueError:
            print("Bonus is not a number!")


class Departments:

    def __init__(self):
        self.departments = dict()

    def add_employer(self, department_name, first_name, last_name, employers_database):

        try:
            for key, val in employers_database.items():
                if val[0] == first_name and val[1] == last_name:
                    self.departments[department_name].append(key)
                    print("Sucessfully added to department!")
                    return 0
            print("No such department or employer!")
        except KeyError:

            print("No such department or employer!")

    def add_department(self, name):

        if name in self.departments.keys():
            print("Department already exists!")
        else:
            self.departments[name] = []
            print("Successfully added department!")

    def display_departments(self):
        print("Current departments in the company: ", list(self.departments.keys()))

    def display_employers_in_department(self, department_name, employers_database):

        try:
            print(f'Employers in department: {department_name}')
            for employer_id in self.departments[department_name]:
                if employer_id in employers_database.keys():
                    print(employers_database[employer_id][0], employers_database[employer_id][1])

        except KeyError:
            print("Invalid department name!")

    def remove_from_department(self, department_name, first_name, last_name, employers_database):
        try:
            for key, val in employers_database.items():
                if val[0] == first_name and val[1] == last_name:
                    self.departments[department_name].remove(key)
                    print("Employer successfully removed!")
        except KeyError:
            print("No such department or employer to remove!")

    def remove_entire_department(self, department_name):
        try:
            del self.departments[department_name]
            print("Successfully removed department!")
        except KeyError:
            print(f'No such department: {department_name}')


def select_user():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    return first_name, last_name


def proceed():
    return input("Press enter to proceed... ")


def find_in_database(first_name, last_name, emp_database, dep_database):
    try:
        for key, val in emp_database.items():
            if val[0] == first_name or val[1] == last_name:
                for keys, values in dep_database.items():
                    if key in values:
                        print(f'{first_name, last_name} works in department: {keys}')
                        return 0
    except KeyError:
        print("No user found! ")
    print("No user found! ")


def export_employer_data(first_name, last_name, emp_database):
    try:
        for key, val in emp_database.items():
            if val[0] == first_name or val[1] == last_name:
                with open('user_data.txt', 'w') as f:
                    f.write(f'Name: {val[0]}, Surname: {val[1]}, Age: {val[2]}, Job: {val[3]}, Salary: {val[4]} '
                            f'Bonus: {val[5]}, Bonus+Salary: {val[6]}')
                print("Data Successfully exported to user_data.txt")

    except KeyError:
        print("No such user found!")


main_message = "Welcome to company management console! \n" \
               "Options for Employer management: \n" \
               "1 - Show all employers \n" \
               "2 - Add employer to database. \n" \
               "3 - Remove Employer from database. \n" \
               "4 - Apply bonus to employer \n" \
               "5 - Apply bonus to employers in entire department \n" \
               "------------ \n" \
               "Options for Departments management: \n" \
               "6 - Display departments \n" \
               "7 - Display employers in department \n" \
               "8 - Add department \n" \
               "9 - Remove department \n" \
               "10 - Add employer to department \n" \
               "11 - Remove employer from department \n" \
               "-----ADVANCED----- \n" \
               "12 - Find employer in department \n" \
               "13 - Export employer data to txt file"

emps = Employers()
deps = Departments()


while True:
    print(main_message)
    option = input("Select operation to perform: ")

    try:
        option = int(option)
    except ValueError:
        continue

    if option == 1:
        emps.show_employers()
        proceed()
        continue

    if option == 2:
        first_name, last_name = select_user()
        age = input("Age: ")
        job = input("Job: ")
        salary = input("Salary (must be a number): ")
        bonus = input("Bonus (must be a number): ")

        emps.add_employer(first_name, last_name, age, job, salary, bonus)
        proceed()
        continue

    if option == 3:
        first_name, last_name = select_user()
        emps.remove_employer(first_name, last_name)
        proceed()
        continue

    if option == 4:
        first_name, last_name = select_user()
        bonus = input("Bonus value: ")
        emps.apply_bonus(first_name, last_name, bonus)
        proceed()
        continue

    if option == 5:
        department_name = input("Department name: ")
        bonus_value = input("Bonus value: ")
        emps.add_bonus_to_entire_department_employers(department_name, bonus_value, deps.departments)
        proceed()
        continue

    if option == 6:
        deps.display_departments()
        proceed()
        continue

    if option == 7:
        department_name = input("Department name: ")
        deps.display_employers_in_department(department_name, emps.employers_database)
        proceed()
        continue

    if option == 8:
        deparment_name = input("Department name: ")
        deps.add_department(deparment_name)
        proceed()
        continue

    if option == 9:
        department_name = input("Department name: ")
        deps.remove_entire_department(department_name)
        proceed()
        continue

    if option == 10:
        department_name = input("Department name: ")
        first_name, last_name = select_user()

        deps.add_employer(department_name, first_name, last_name, emps.employers_database)
        proceed()
        continue

    if option == 11:
        department_name = input("Department name: ")
        first_name, last_name = select_user()
        deps.remove_from_department(department_name, first_name, last_name, emps.employers_database)
        proceed()
        continue

    if option == 12:
        first_name, last_name = select_user()
        find_in_database(first_name, last_name, emps.employers_database, deps.departments)
        proceed()
        continue

    if option == 13:
        first_name, last_name = select_user()
        export_employer_data(first_name, last_name, emps.employers_database)
        proceed()
        continue
