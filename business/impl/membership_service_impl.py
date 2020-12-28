from business.impl.command.membership.find_all import FindAll
from business.impl.command.membership.find import Find

from business.membership_service import MembershipService


class MembershipServiceImpl(MembershipService):

    def find_all(self, filters):
        return FindAll(filters).execute()

    def find(self):
        return Find(self).execute()

    # TODO: Review what params we need to create a new membership
    def new_membership(self): raise NotImplementedError
