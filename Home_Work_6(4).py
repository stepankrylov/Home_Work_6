class Car:
    def __init__(self, speed, color, name, is_police: bool, direction):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_police
        self.d = direction

    def go(self):
        if self.s > 0:
            return f'{self.n} поехал(-а)'

    def stop(self):
        if self.s == 0:
            return f'{self.n} остановился(-лась)'

    def turn(self):
        if self.d != '':
            return f'{self.n} повернул(-а) {self.d}'

    def show_speed(self):
        return f'Скорость {self.n} составляет {self.s} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            return f'Скорость {self.n} превышена на {self.s - 60} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            return f'Скорость {self.n} превышена на {self.s - 40} км/ч'


class SportCar(Car):
    def show_car(self):
        return f'{self.c} {self.n}'


class PoliceCar(Car):
    def show_police(self):
        if self.p:
            return f'{self.n} - полиция'


c = Car(0, 'Зелёный', 'Fiat', False, '')
print(c.go())
print(c.stop())
print(c.turn())
print(c.show_speed())
tc = TownCar(80, 'Серебристый', 'Nissan', False, 'налево')
print(tc.show_speed())
wc = WorkCar(80, 'Синий', 'Cat', False, '')
print(wc.show_speed())
sc = SportCar(0, 'Красный', 'Audi', False, '')
print(sc.show_car())
pc = PoliceCar(80, 'Белый', 'Ford', True, '')
print(pc.show_police())


