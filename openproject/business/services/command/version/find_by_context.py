from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.version.version_command import VersionCommand
from openproject.model import version as v


class FindByContext(VersionCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return v.Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding version by context: {self.context}") from re