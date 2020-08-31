class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        return f'Для предмета "{self.t}" запускается отрисовка'


'''
Включил self.t в функцию draw, чтобы функция draw не стала статичной
'''


class Pen(Stationery):
    def draw(self):
        if self.t == 'ручка':
            return f'Для ручки запускается отрисовка'


class Pencil(Stationery):
    def draw(self):
        if self.t == 'карандаш':
            return f'Для карандаша запускается отрисовка'


class Handle(Stationery):
    def draw(self):
        if self.t == 'маркер':
            return f'Для маркера запускается отрисовка'


s = Stationery('степлер')
print(s.draw())

pen = Pen('ручка')
print(pen.draw())
pen = Pen('бумага')
print(pen.draw())

pencil = Pencil('карандаш')
print(pencil.draw())
pencil = Pencil('бумага')
print(pencil.draw())

handle = Handle('маркер')
print(handle.draw())
handle = Handle('бумага')
print(handle.draw())
