from abc import ABCMeta, abstractmethod


class IProbCalculator(metaclass=ABCMeta):

    @abstractmethod
    def prob_class(self, class_number):
        """
        そのクラスに所属する確率を算出する
        :param class_number: 求める対象となるクラス
        :return:$p(class_number)$の値
        """
        pass

    @abstractmethod
    def prob_data_index(self, index: int, data_value: int)->float:
        """
        index番目のデータの値がdata_valueである確率を算出する
        :param index:配列のインデックス
        :param data_value:当該するデータの値
        :return:$p_{index}(data_value)$の値
        """
        pass

    @abstractmethod
    def prob_data_index_and_class(self, index: int, data_value: int, class_number: int)->float:
        """
        index番目のデータの値がdata_valueであり,かつ所属しているクラスがclass_numberである確率を求める
        ここではそれぞれの条件は独立であると仮定する
        :param index:配列のインデックス
        :param data_value:当該するデータの値
        :param class_number: 求める対象となるクラス
        :return:
        """
        pass

    @abstractmethod
    def prob_data_index_in_class(self, index: int, data_value: int, class_number: int)->float:
        """
        指定したクラスに所属しているという条件で指定したインデックスのデータが指定した値になっているという条件付き確率を求める
        :param index:データのインデックス
        :param data_value:データの値
        :param class_number:所属しているクラス
        :return:指定したクラスに所属しているという条件での条件付確率
        """
        pass


class ProbCalculator(IProbCalculator):
    def __init__(self, data_holder):
        self.__data_holder = data_holder
        self.__memo_prob_data_index_and_class = {}  # Dict[Tuple[int, int, int] float]
        self.__memo_prob_data_index_in_class = {}  # Dict[Tuple[int, int, int] float]
        self.__memo_data_index = {}  # Dict[Tuple[int, int], float]
        self.__memo_prob_class = {}  # Dict[int, float]

    @property
    def data_holder(self):
        return self.__data_holder

    def prob_class(self, class_number: int)-> float:
        """
        そのクラスに所属する確率を算出する
        :param class_number: 求める対象となるクラス
        :return:$p(class_number)$の値
        """
        if class_number in self.__memo_prob_class:
            return self.__memo_prob_class[class_number]
        data_num = self.data_holder.extract_class(class_number).count
        prob = data_num/self.data_holder.count
        self.__memo_prob_class[class_number] = prob
        return prob

    def prob_data_index(self, index: int, data_value: int)->float:
        """
        index番目のデータの値がdata_valueである確率を算出する
        :param index:配列のインデックス
        :param data_value:当該するデータの値
        :return:$p_{index}(data_value)$の値
        """
        if (index, data_value) in self.__memo_data_index:
            return self.__memo_data_index[(index, data_value)]
        data_num = self.data_holder.extract_data_index(index, data_value)
        prob = data_num/self.data_holder.count
        self.__memo_prob_data_index_in_class[(index, data_value)] = prob
        return prob

    def prob_data_index_and_class(self, index: int, data_value: int, class_number: int)->float:
        """
        index番目のデータの値がdata_valueであり,かつ所属しているクラスがclass_numberである確率を求める
        ここではそれぞれの条件は独立であると仮定する
        :param index:配列のインデックス
        :param data_value:当該するデータの値
        :param class_number: 求める対象となるクラス
        :return:
        """
        if (index, data_value, class_number) in self.__memo_prob_class:
            return self.__memo_prob_class[(index, data_value, class_number)]
        prob_data_value_index = self.prob_data_index(index, data_value)
        prob_class = self.prob_class(class_number)
        prob = prob_data_value_index*prob_class
        self.__memo_prob_class[(index, data_value, class_number)] = prob
        return prob

    def prob_data_index_in_class(self, index: int, data_value: int, class_number: int)->float:
        """
        指定したクラスに所属しているという条件で指定したインデックスのデータが指定した値になっているという条件付き確率を求める
        :param index:データのインデックス
        :param data_value:データの値
        :param class_number:所属しているクラス
        :return:指定したクラスに所属しているという条件での条件付確率
        """
        if (index, data_value, class_number) in self.__memo_prob_data_index_in_class:
            return self.__memo_prob_data_index_in_class[(index, data_value, class_number)]
        prob = self.prob_data_index_and_class(index, data_value, class_number)/self.prob_class(class_number)
        self.__memo_prob_data_index_in_class[(index, data_value, class_number)] = prob
        return prob


