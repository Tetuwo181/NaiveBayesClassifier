from parts.prob_calculator import IProbCalculator
from parts import data_holder as dh
import numpy as np


class Model(object):
    def __init__(self, prob_calculator: IProbCalculator,  class_num: int):
        self.__prob_calculator = prob_calculator
        self.__class_index_set = np.arange(class_num)
        self.__class_num = class_num

    def calc_fitness_value(self, data: np.ndarray, class_number: int)-> float:
        """
        モデルの適合度を算出する
        :param data:
        :param class_number:
        :return:
        """
        vectorized_calculator = np.frompyfunc(self.__prob_calculator.prob_data_index_in_class, 3, 1)
        index_set = np.arange(len(data))
        prob_set = vectorized_calculator(index_set, data, class_number)
        return np.prod(prob_set)*self.__prob_calculator.prob_class(class_number)

    def predict(self, data: np.ndarray)->int:
        """
        モデルの適合度から該当するクラスを算出する
        :param data: 算出対象となるデータ
        :return: 一番適合度が高いクラス
        """
        fitness_set = np.array([self.calc_fitness_value(data, index) for index in self.__class_index_set])
        return np.argmax(fitness_set)

    def test(self, data_set: np.ndarray, class_set: np.ndarray)->float:
        predicted_set = np.array([self.predict(data) for data in data_set])
        # 教師データと予測されたデータの差が0でなければ誤判定
        diff = class_set - predicted_set
        return np.sum(diff == 0)/len(data_set)






