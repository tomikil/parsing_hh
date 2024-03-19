from abc import ABC, abstractmethod


class JSONSaverAbstract(ABC):
    @abstractmethod
    def get_list_vacancy(self, vacancies):
        pass

    @abstractmethod
    def add_vacancy(self, list_vacancy, file):
        pass

    @abstractmethod
    def delete_vacancy(self, file):
        pass