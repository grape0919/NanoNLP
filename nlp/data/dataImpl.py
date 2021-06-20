from abc import ABCMeta, abstractmethod

class DataImpl(ABCMeta):


    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def reset(self):
        pass