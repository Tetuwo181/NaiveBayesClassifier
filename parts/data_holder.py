import pandas as pd


class DataHolder(object):
    """
    学習に使うデータを保持するクラス
    """
    def __init__(self, data_set, class_set):
        """
        コンストラクタ
        :param data_set: 学習に使う元となるデータセット numpy配列を保持したリストもしくはそれをnumpy配列にしたもの。各要素はint型
        :param class_set 各データのクラスのセット
        :return:
        """
        self.__data_frame = pd.DataFrame({"data": data_set, "class": class_set})

    @property
    def data_set(self):
        return self.__data_frame["data"].values

    @property
    def class_set(self):
        return self.__data_frame["class"].values

    @property
    def count(self):
        return len(self.data_set)

    def extract_class(self, class_number: int):
        """
        指定したクラスのデータを取得する
        :param self:
        :param class_number: 抽出したいクラスのインデックス。整数型
        :return: データ抽出後のDataHolderクラスのインスタンス
        """
        data_and_classes = [(data, class_index) for data, class_index in zip(self.data_set, self.class_set)
                            if class_index == class_number]
        return DataHolder([value[0] for value in data_and_classes], [value[1] for value in data_and_classes])

    def extract_data_index(self, index: int, data_value: int):
        """
        指定したデータの値を抽出する
        :param index: 指定したいデータの属性のインデックス
        :param data_value: 抽出したい値　整数型
        :return: データ抽出後のDataHolderクラスのインスタンス
        """
        data_and_classes = [(data, class_index) for data, class_index in zip(self.data_set, self.class_set)
                            if data[index] == data_value]
        return DataHolder([value[0] for value in data_and_classes], [value[1] for value in data_and_classes])

    def extract_class_and_index(self, index, data_value, class_number):
        """
        指定した数値の条件とクラスを抽出する
        :param index:指定したいデータの属性のインデックス
        :param data_value:抽出したい値　整数型
        :param class_number:抽出したいクラスのインデックス。整数型
        :return:データ抽出後のDataHolderクラスのインスタンス
        """
        return self.extract_data_index(index, data_value).extract_class(class_number)


def build_df(data_set: pd.core.frame.DataFrame):
    return DataHolder(data_set["data_set"], data_set["class"])


def build(data_set, class_set=None):
    """
    引数が1つの時はpandasのデータフレームから
    2津の時は1番目がデータの値で2番目がクラスの値のセットとなる
    :param data_set:
    :param class_set:
    :return:
    """
    if class_set is None:
        return build_df(data_set)
    return DataHolder(data_set, class_set)
