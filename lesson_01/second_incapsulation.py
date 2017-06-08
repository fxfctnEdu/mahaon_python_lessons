class Figure:
    count = 0

    def __init__(self, name):
        self.__name = name
        Figure.count += 1

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def info(self):
        print('Имя: ', self.__name,
              '\nВсего фигур: ', Figure.count)


# main
red_figure = Figure('Фигура красная')
print(red_figure.get_name())
red_figure.set_name('Белая!')
print(red_figure.get_name())
