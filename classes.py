# learn classes
# https://www.youtube.com/watch?v=rq8cL2XMM5M


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):

    def __init__(self, first, last, pay, position):
        super().__init__(first, last, pay)
        self.position = position


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emp(self):
        for emp in self.employees:
            if hasattr(emp, 'position'):
                print('--> ' + emp.fullname() + ' working as ' + emp.position)
            else:
                print('--> ' + emp.fullname())

    def __str__(self):
        return ('{} {}'.format(self.first, self.last) +
                ' has salary {}'.format(self.pay))


emp_1 = Employee('Mateusz', 'Kac', 20000)
dev_1 = Developer('Marcin', 'Jackowicz', 10000, 'Java')
mgr_1 = Manager('Mariusz', 'Jakubiak', 20000)
mgr_1.add_emp(emp_1)
mgr_1.add_emp(dev_1)
mgr_1.show_emp()
print(str(mgr_1))
