from parts import data_holder as dh
from parts import prob_calculator as pb
from parts import model


class Trainer(object):
    def __init__(self, class_num: int):
        self.__class_num = class_num

    def train(self, train_data, train_class):
        data_holder = dh.DataHolder(train_data, train_class)
        prob_calculator = pb.ProbCalculator(data_holder)
        return model.Model(prob_calculator, self.__class_num)

