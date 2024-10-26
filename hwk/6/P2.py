class Person:
    def __init__(self, name, address, telephone):
        self._name = name
        self._address = address
        self._telephone = telephone

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_telephone(self):
        return self._telephone

    def set_telephone(self, telephone):
        self._telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        super().__init__(name, address, telephone)
        self._customer_number = customer_number
        self._on_mailing_list = on_mailing_list

    def get_customer_number(self):
        return self._customer_number

    def set_customer_number(self, customer_number):
        self._customer_number = customer_number

    def get_on_mailing_list(self):
        return self._on_mailing_list

    def set_on_mailing_list(self, on_mailing_list):
        self._on_mailing_list = on_mailing_list

    def display_details(self):
        print(f"Name: {self.get_name()}")
        print(f"Address: {self.get_address()}")
        print(f"Telephone: {self.get_telephone()}")
        print(f"Customer Number: {self.get_customer_number()}")
        print(f"On Mailing List: {'Yes' if self.get_on_mailing_list() else 'No'}")

customer = Customer("John Doe", "123 Main St, Anytown, USA", "555-1234", 1001, True)

customer.display_details()
