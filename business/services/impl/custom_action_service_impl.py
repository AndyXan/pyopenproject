from business.services.custom_action_service import CustomActionService
from business.services.impl.command.custom_action.execute import Execute
from business.services.impl.command.custom_action.find import Find


class CustomActionServiceImpl(CustomActionService):

    def execute(self, custom_action):
        return Execute(custom_action).execute()

    def find(self, custom_action):
        return Find(custom_action).execute()