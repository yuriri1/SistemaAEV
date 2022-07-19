from abc import ABC, abstractmethod
import pickle


class DAO(ABC):
    @abstractmethod
    def __init__(self, arquivo=" "):
        self.__arquivo = arquivo
        self.__cache = {}
        self.__load()

    def __load(self):
        self.__cache = pickle.load(open(self.__arquivo, 'rb'))

    def __dump(self):
        pickle.dump(self.__cache, open(self.__arquivo, 'wb'))

    def adiciona(self, chave, obj):
        self.__cache[chave] = obj
        self.__dump()

    def pega(self, chave):
        try:
            return self.__cache[chave]
        except KeyError:
            return None

    def remove(self, chave):
        try:
            self.__cache.pop(chave)
            self.__dump()
        except KeyError:
            return None

    def pega_tudo(self):
        return self.__cache.values()
