import calendar
import math
from datetime import datetime

from const import InputData, MetrologicalParams
from data_models import (
    CalculatedMP,
    MElevation,
    SquareDeviation,
    TroposphericCorrection
)


def current_day_count(observation_timestamp: int) -> int:
    cur_date = datetime.fromtimestamp(observation_timestamp)

    # Вычисляем ближайший високосный год
    leap_year = cur_date.year
    while not calendar.isleap(leap_year):
        leap_year -= 1

    # Номер суток в текущем четырёхлетии
    n_t = cur_date - datetime(year=leap_year, day=1, month=1)
    n_t = n_t.days

    cur_day = 0
    if n_t <= 366:
        cur_day = n_t
    elif 367 <= n_t <= 731:
        cur_day = n_t - 366
    elif 732 <= n_t <= 1096:
        cur_day = n_t - 731
    elif n_t >= 1097:
        cur_day = n_t - 1096

    return cur_day


def _get_calculated_mp(avg: float, delta: float, cur_day: int) -> float:
    d_min = 28  # Для северных широт
    return avg - delta * math.cos(
            (2 * math.pi * (cur_day - d_min)) / 365.25)


def get_calculated_metrological_params(cur_day: int) -> CalculatedMP:
    calculated_mp_args = {
        key: _get_calculated_mp(avg=value['avg'],
                                delta=value['delta'],
                                cur_day=cur_day)
        for key, value in MetrologicalParams.calc_mapping.items()
    }
    return CalculatedMP(**calculated_mp_args)


def _get_m_el(elevation: float) -> float:
    _base_el = 1.001 / math.sqrt(0.002001 + math.sin(
        math.radians(elevation)
    )**2)

    m_elevation = _base_el
    if 2 <= elevation <= 4:
        return _base_el * (1 + 0.015*(4-elevation)**2)
    return m_elevation


def get_m_elevation(elevation: float) -> MElevation:
    m_elevation_args = {
        'custom_degrees': _get_m_el(elevation),
        'degrees45': _get_m_el(45),
        'degrees90': _get_m_el(90)
    }

    return MElevation(**m_elevation_args)


def get_tropospheric_correction(calc_mp: CalculatedMP,
                                m_el: MElevation) -> TroposphericCorrection:
    ip = InputData()

    z_hyd = (10 ** -6 * ip.k1 * ip.r_d * calc_mp.p) / ip.g_m
    z_wet = (
                (10 ** -6 * ip.k2 * ip.r_d) /
                ((ip.g_m * (calc_mp.lambda_ + 1)) - (calc_mp.beta * ip.r_d))
            ) * (calc_mp.e / calc_mp.t)

    _d_base = (1 - (calc_mp.beta * ip.h / calc_mp.t))

    d_hyd = (_d_base ** (ip.g / ip.r_d / calc_mp.beta)) * z_hyd
    d_wet = _d_base ** (
            ((calc_mp.lambda_ + 1) * ip.g / ip.r_d / calc_mp.beta) - 1
    ) * z_wet

    _tc_base = -(d_hyd + d_wet)
    tc_custom = _tc_base * m_el.custom_degrees
    tc_45_deg = _tc_base * m_el.degrees45
    tc_90_deg = _tc_base * m_el.degrees90

    return TroposphericCorrection(custom_degrees=tc_custom,
                                  degrees45=tc_45_deg,
                                  degrees90=tc_90_deg,
                                  z_wet=z_wet,
                                  d_wet=d_wet)


def get_square_deviation(m_el: MElevation) -> SquareDeviation:
    sigma_custom_deg = 0.12 * m_el.custom_degrees
    sigma_45_deg = 0.12 * m_el.degrees45
    sigma_90_deg = 0.12 * m_el.degrees90

    return SquareDeviation(custom_degrees=sigma_custom_deg,
                           degrees45=sigma_45_deg,
                           degrees90=sigma_90_deg)
