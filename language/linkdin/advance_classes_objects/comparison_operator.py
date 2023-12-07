# Comparison functions
# object.__lt__(self, other) - less than (<) operator call when self < other
# object.__le__(self, other) - less than or equal to (<=) operator call when self <= other
# object.__eq__(self, other) - equal to (==) operator call when self == other
# object.__ne__(self, other) - not equal to (!=) operator call when self != other
# object.__gt__(self, other) - greater than (>) operator call when self > other
# object.__ge__(self, other) - greater than or equal to (>=) operator call when self >= other


# use special methods to compare objects to each other

class Employee:
    def __init__(self, f_name, l_name, level, yrs_service):
        self.f_name = f_name
        self.l_name = l_name
        self.level = level
        self.seniority = yrs_service

    # # implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    #
    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    #
    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    #
    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    #
    def __eq__(self, other):
        return self.level == other.level


def main():
    # define some employees
    dept = [Employee("Tim", "Sims", 5, 9), Employee("John", "Doe", 4, 12), Employee("Jane", "Smith", 6, 6),
            Employee("Rebecca", "Robinson", 5, 13), Employee("Tyler", "Durden", 5, 12)]

    # dept = []
    # dept.append(Employee("Tim", "Sims", 5, 9))
    # dept.append(Employee("John", "Doe", 4, 12))
    # dept.append(Employee("Jane", "Smith", 6, 6))
    # dept.append(Employee("Rebecca", "Robinson", 5, 13))
    # dept.append(Employee("Tyler", "Durden", 5, 12))
    # print(dept)

    # TODO: Who's more senior?
    print(bool(dept[0] > dept[2]))  # False
    print(bool(dept[4] < dept[3]))  # True

    # TODO: sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.l_name)


if __name__ == "__main__":
    main()