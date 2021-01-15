from business.services.impl.command.user.create import Create
from business.services.impl.command.user.delete import Delete
from business.services.impl.command.user.find import Find
from business.services.impl.command.user.find_all import FindAll
from business.services.impl.command.user.lock import Lock
from business.services.impl.command.user.unlock import Unlock
from business.services.impl.command.user.update import Update
from business.services.user_service import UserService


class UserServiceImpl(UserService):

    def lock_user(self, user):
        return Lock(user).execute()

    def unlock_user(self, user):
        return Unlock(user).execute()

    def find_all(self, offset, pageSize, filters, sortBy):
        return FindAll(offset, pageSize, filters, sortBy).execute()

    def find(self, user):
        return Find(user).execute()

    def update_user(self, user):
        return Update(user).execute()

    def delete_user(self, user):
        Delete(user).execute()

    def create_user(self, user):
        return Create(user).execute()