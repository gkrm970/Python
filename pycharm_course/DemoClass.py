class DemoSuperClass:
    demo_zip_1 = ""
    demo_city = ""


class DemoPython(DemoSuperClass):
    demo_name = ""

    def __init__(self, a, b) -> None:
        c = 10 + 20
        self.demo_zip_1 = 100
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()

    def add_numbers(self, c, a1, b, d):
        return a1 + b

    def print_name(self, name_1):
        name_of_user_first = name_1
        print(name_of_user_first)


if __name__ == '__main__':
    d = DemoPython(10, 20)
    print(d.add_numbers(100, 10, 20, 200))
    print(d.add_numbers(100, 20, 30, 200))
    print(d.add_numbers(100, 30, 40, 200))
    print(d.add_numbers(100, 50, 70, 200))
