class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def mass(self):
        depth = 0.05
        dense = 1100
        m = self._l * self._w * depth * dense
        return f'Для покрытия дорожного полотна длиной {self._l/1000} км ({self._l} м),\n' \
               f'шириной {self._w} м и толщиной {depth} м (или {depth*100} см)\n' \
               f'потребуется {m} кг или {m/1000} тонн асфальта (плотность {dense} кг на м^3)'


r = Road(5000, 10)
print(r.mass())
