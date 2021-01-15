from abc import ABCMeta, abstractmethod


class StatusService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self): raise NotImplementedError

    @abstractmethod
    def find(self, status): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError