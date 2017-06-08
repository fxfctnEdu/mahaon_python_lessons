class Figure:
    # переменная класса. сколько всего элеметов создано
    count = 0

    # конструктор класса. вызывается при создании экземпляра
    def __init__(self, name, color):
        # переменные экзампляра класса. их значения доступны только объекту
        self.color = color
        self.name = name
        # увеличиваем значение переменной класса
        Figure.count += 1

    def info(self):
        print('Имя: ', self.name,
              '\nЦвет: ', self.color,
              '\nВсего фигур: ', Figure.count)


#main
red_figure = Figure('Фигура красная', 'Красный')
red_figure.info()
white_figure = Figure('Фигура белая', 'Красный')
white_figure.info()

#print(red_figure.color)
