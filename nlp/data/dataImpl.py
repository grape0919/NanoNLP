from abc import ABCMeta, abstractmethod

class DataImpl(ABCMeta):


    @abstractmethod
    def reset(self):
        pass