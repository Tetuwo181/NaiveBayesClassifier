from typing import Callable
import numpy as np


def sample(divide_num: int, min_value: float=0, max_value: float=1.0)->Callable[[float], int]:
    """
    0から1.0までの値に対して入力した数の分だけ分割する
    :param divide_num: 分割数
    :return:
    """
    def use_func(value: float)->int:
        boundary_set = np.linspace(min_value, max_value, divide_num+1)
        boundary_min_set = boundary_set[:-1]
        boundary_max_set = boundary_set[1:]
        for index, (boundary_min, boundary_max) in enumerate(zip(boundary_min_set, boundary_max_set)):
            if boundary_min <= value < boundary_max:
                return index
        return divide_num
    return use_func
