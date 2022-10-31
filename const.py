class MetrologicalParams:
    """Метрологические параметры для вычисления тропосферной задержки
    при широте 60 град. """ 

    # Средние значения параметров
    p0 = 1011.75     # P_0, мбар
    t0 = 272.15      # T_0, К
    e0 = 6.78        # e_0, мбар
    beta0 = 0.00539  # Beta_0, К/м
    lambda0 = 1.81

    # Сезонное изменение параметров
    delta_p = -1.75  # Delta_P, мбар
    delta_t = 15.00  # Delta_K, К
    delta_e = 5.36   # Delta_e, мбар
    delta_beta = 0.00081  # Delta_Beta К/м
    delta_lambda = 0.74

    calc_mapping = {
        'p': {'avg': p0, 'delta': delta_p},
        't': {'avg': t0, 'delta': delta_t},
        'e': {'avg': e0, 'delta': delta_e},
        'beta': {'avg': beta0, 'delta': delta_beta},
        'lambda_': {'avg': lambda0, 'delta': delta_lambda},
    }


class InputData:
    """Входные данные для решения задачи вычисления тропосферной задержки"""
    observation_timestamp = 1665838800  # 15.10.2022  16:00:00
    consumer_latitude = 55.76581124     # Широта, град
    # Высота потребителя над уровнем моря, м
    h = 200.694                          
    elevation = 13.7690                 # Угол места, град
    g = 9.80665                         # Ускорение свободного падения м/с^2
    k1 = 77.604                         # К/мбар
    k2 = 382000                         # K^2/мбар
    g_m = 9.784                         # м/с^2
    r_d = 287.054                       # Дж*кг^−1*K^−1
