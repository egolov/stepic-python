class Buffer:
    def __init__(self):
        self.items = list()
        # конструктор без аргументов

    def add(self, *a):
        # добавить следующую часть последовательности
        for item in a:
            self.items.append(item)
            if len(self.items) == 5:
                print(sum(self.items))
                self.items.clear()

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.items


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print([6] == buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print([] == buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print([1] == buf.get_current_part()) # вернуть [1]