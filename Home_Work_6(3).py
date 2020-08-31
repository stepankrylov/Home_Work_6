class Worker:
    def __init__(self, name, surname, position, income):
        self.n = name
        self.s = surname
        self.p = position
        self._i = income


class Position(Worker):
    def get_full_name(self):
        return f'Имя работника {self.n} {self.s}'

    def get_total_income(self):
        return f'Доход работника {self._i["wage"] + self._i["bonus"]}'


income = {'wage': 1000, 'bonus': 500}
w = Worker('adam', 'smith', 'position', income)
p = Position('adam', 'smith', 'position', income)
print(p.get_full_name())
print(p.get_total_income())
