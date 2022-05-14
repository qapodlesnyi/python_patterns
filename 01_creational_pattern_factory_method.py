'''
Тип: 
    Пораждающий паттерн.
Используется когда:
    - абстрактому базовому классу зарание ниезвестно, экземплыры каких конкретных классов ему могу понадобится;
    - необходмо легко вводить новые классы, объектры котороых нужно создавать;
    - необходимо установить связь между паралельными иерархиями классов
'''


from abc import ABCMeta, abstractstaticmethod

# ===========================================================================================

class Specialization(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_specialization(): pass

    @abstractstaticmethod
    def get_identifier(): pass

class Developer(Specialization):
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._specialization = "Developer"

    def get_specialization(self):
        return (self._specialization)

    def get_identifier(self):
        return (f"{self._name}_{self._surname}")


class DevOps(Specialization):
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._specialization = "DevOps"
    
    def get_specialization(self):
        return (self._specialization)
    
    def get_identifier(self):
        return (f"{self._name}_{self._surname}")

# ===========================================================================================

class EmployeeCreator(metaclass=ABCMeta):
    @abstractstaticmethod
    def create_employee(): pass


class DeveloperCreator(EmployeeCreator):
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def create_employee(self):
        return Developer(self._name, self._surname)


class DevOpsCreator(EmployeeCreator):
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def create_employee(self): 
        return DevOps(self._name, self._surname)

# ===========================================================================================

# FIRST VARIANT OF USING: ___________________________________________________________________
employee = DeveloperCreator("oleg", "podlesny").create_employee()
print (f"{employee.get_identifier()}: {employee.get_specialization()}")

# SECOND VARIANT OF USING: __________________________________________________________________
def create_employee_factory(employee: EmployeeCreator):
    return employee.create_employee()


identifier = DeveloperCreator("anton", "komolov")
employee = create_employee_factory(identifier)
print (f"{employee.get_identifier()}: {employee.get_specialization()}") 

# SECOND VARIANT OF USING: ___________________________________________________________________
class EmployeeFactory():
    @staticmethod
    def create_employee_factory(specialisation, name, surname):
        if specialisation == "Developer":
            return Developer(name, surname)
        elif specialisation == "DevOps":
            return DevOps(name, surname)
        else:
            print (f"Invalid specialisation: {specialisation}")

nikolaj_semenov = EmployeeFactory.create_employee_factory("DevOps", "nikolaj", "semenov")
print (f"{nikolaj_semenov.get_identifier()}: {nikolaj_semenov.get_specialization()}")
