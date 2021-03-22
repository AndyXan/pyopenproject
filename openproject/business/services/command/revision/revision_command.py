from abc import abstractmethod, ABCMeta

from openproject.business.services.command.command import Command


class RevisionCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/revisions"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError