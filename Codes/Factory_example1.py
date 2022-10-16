# Product
class Employee:
    def test(self):
        print("Employee")


# ConcreteProduct
class Manager(Employee):
    def test(self):
        print("Manager")


# Creator
class Creator:
    # FactoryMethod
    def create_employee(self):
        return Employee()

    # Some operation
    def test(self):
        self.create_employee().test()


# ConcreteCreator
class ManagerCreator(Creator):
    # FactoryMethod
    def create_employee(self):
        return Manager()


# Client
creator = Creator()
creator.test()
# printed: Employee

creator = ManagerCreator()
creator.test()
# printed: Manager
