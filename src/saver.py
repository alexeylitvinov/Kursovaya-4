from abc import ABC, abstractmethod


class Saver(ABC):
    pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass
