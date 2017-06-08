class Figure:
    count = 0

    def __init__(self, name, color):
        self.color = color
        self.name = name
        Figure.count += 1

    def info(self):
        print('Имя: ', self.name,
              '\nЦвет: ', self.color,
              '\nВсего фигур: ', Figure.count)

    # decorator. Thank you, python 3
    @staticmethod
    def class_info():
        # статический метод, достун через имя класса, может быть вызван, когда не создан ни один объект
        # self не передается
        print('Всего фигур: ', Figure.count)


class Circle(Figure):
    def __init__(self, name, color, point, radius):
        # В производном классе необходимо вызвать метод инициализации родителя.
        super().__init__(name, color)
        # инициализируем поля объекта класса потомка
        self.point = point
        self.radius = radius

    def info(self):
        # переопределяем метод базового (родительского) класса
        print('Имя: ', self.name,
              '\nЦвет: ', self.color,
              '\nЦентр: ', self.point,
              '\nРадиус: ', self.radius,
              '\nВсего фигур: ', Figure.count)

    def call_parent_method(self):
        # super() возвращает ссылку на объект родителя,
        # через эту ссылку мы можем вызвать методы родителя
        # в методах потомка
        super().class_info()


# main
red_figure = Figure('Фигура красная', 'Красный')
red_figure.info()
circle = Circle('Круг 1', 'Белый', (10, 12), 5)
circle.info()
Figure.class_info()
Circle.class_info()
circle.call_parent_method()
