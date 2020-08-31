import time as tm


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print('Красный свет')
            tm.sleep(7)
            print('Жёлтый свет')
            tm.sleep(2)
            print('Зелёный свет')
            tm.sleep(4)
        else:
            print('Нарушен режим работы светофора')


t = TrafficLight('red')
t.running()
