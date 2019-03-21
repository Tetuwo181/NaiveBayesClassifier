from parts.prob_calculator import IProbCalculator
from parts import data_holder as dh
import numpy as np


class Model(object):
    def __init__(self, prob_calculator: IProbCalculator,  class_num: int):
        self.__prob_calculator = prob_calculator
        self.__class_index_set = np.arange(class_num)
        self.__class_num = class_num

    def calc_fitness_value(self, data: np.ndarray, class_number: int)->float:
        """
        モデルの適合度を算出する
        :param data:
        :param class_number:
        :return:
        """
        vectorized_calculator = np.frompyfunc(self.__prob_calculator.prob_data_index_in_class, 3, 1)
        index_set = np.arange(len(data))
        prob_set = vectorized_calculator(data, index_set, class_number)
        return np.prod(prob_set)

    def predict(self, data: np.ndarray)->int:
        """
        モデルの適合度から該当するクラスを算出する
        :param data: 算出対象となるデータ
        :return: 一番適合度が高いクラス
        """
        vectorized_fitness_calculator = np.frompyfunc(self.__prob_calculator.prob_data_index_in_class, 2, 1)
        fitness_set = vectorized_fitness_calculator(data, self.__class_index_set)
        return np.argmax(fitness_set)


