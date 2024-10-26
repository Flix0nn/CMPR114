class Employee:
    def __init__(self, name, employee_id):
        self._name = name
        self._employee_id = employee_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

class ShiftSupervisor(Employee):
    def __init__(self, name, employee_id, annual_salary, annual_production_bonus):
        super().__init__(name, employee_id)
        self._annual_salary = annual_salary
        self._annual_production_bonus = annual_production_bonus

    def get_annual_salary(self):
        return self._annual_salary

    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary

    def get_annual_production_bonus(self):
        return self._annual_production_bonus

    def set_annual_production_bonus(self, annual_production_bonus):
        self._annual_production_bonus = annual_production_bonus

    def display_details(self):
        print(f"Name: {self.get_name()}")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Annual Salary: ${self.get_annual_salary()}")
        print(f"Annual Production Bonus: ${self.get_annual_production_bonus()}")

shift_supervisor = ShiftSupervisor("Alice Johnson", 12345, 75000, 5000)

shift_supervisor.display_details()
