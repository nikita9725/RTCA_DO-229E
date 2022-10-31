from dataclasses import dataclass

from const import InputData


@dataclass
class DegreesBase:
    custom_degrees: float
    degrees45: float
    degrees90: float


@dataclass
class CalculatedMP:
    """Класс с расчитанными метрологическими параметрами"""
    p: float
    t: float
    e: float
    beta: float
    lambda_: float

    def __repr__(self):
        return ('Метрологические параметры:\n'
                f'Давление, мбар P={self.p}\n'
                f'Температура, К T={self.t}\n'
                f'Давление насыщенных водяных паров, мбар e={self.e}\n'
                f'Зависимость температуры от высоты, К/м beta={self.beta}\n'
                f'Градиент изменения испарения воды lambda={self.lambda_}\n')


@dataclass
class MElevation(DegreesBase):
    """Класс с расчитанными значениями функции m(El)"""
    def __repr__(self):
        return ('Расчёт функции тропосферной коррекции:\n'
                f'm({InputData.elevation}) = {self.custom_degrees}\n'
                f'm(45) = {self.degrees45}\n'
                f'm(90) = {self.degrees90}\n')


@dataclass
class TroposphericCorrection(DegreesBase):
    """Класс с расчитанным значением тропосферной поправки"""
    def __repr__(self):
        return ('Расчёт тропосферной поправки для углов места:\n'
                f'{InputData.elevation} град: {self.custom_degrees} м\n'
                f'45 град: {self.degrees45} м\n'
                f'90 град: {self.degrees90} м\n')


@dataclass
class SquareDeviation(DegreesBase):
    """Класс с расчитанными значениями среднеквадратического отклонения
    ошибки вычисления тропосферной поправки  """
    def __repr__(self):
        return('Расчёт срднеквадратического отклонения ошибки вычисления '
               'тропосферной поправки для углов места:\n'
               f'{InputData.elevation} град: {self.custom_degrees} м\n'
               f'45 град: {self.degrees45} м\n'
               f'90 град: {self.degrees90} м\n')
