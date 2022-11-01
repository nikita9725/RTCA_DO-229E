from calc_funcs import (
    current_day_count,
    get_calculated_metrological_params,
    get_m_elevation,
    get_square_deviation,
    get_tropospheric_correction
)
from const import InputData

current_day = current_day_count(InputData.observation_timestamp)
print(f'Текуший день в году: {current_day}\n')

# Расчитанные метрологические параметры
calculated_mp = get_calculated_metrological_params(current_day)
print(calculated_mp)

# Расчитанная функция тропосферной коррекции
m_elevation = get_m_elevation(InputData.elevation)
print(m_elevation)

tropospheric_correction = get_tropospheric_correction(calc_mp=calculated_mp,
                                                      m_el=m_elevation)
print(tropospheric_correction)

# Среднеквадратическое отклонение
square_deviation = get_square_deviation(m_elevation)
print(square_deviation)
