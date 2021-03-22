from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from openproject.business.util.filters import Filters
from openproject.business.util.url import URL
from openproject.business.util.url_parameter import URLParameter
from openproject.model.time_entry import TimeEntry


class FindAll(TimeEntryCommand):

    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                          [
                                                              Filters(
                                                                  self.filters),
                                                              URLParameter("sortBy", self.sort_by)
                                                          ])))
            return FindListCommand(self.connection, request, TimeEntry).execute()

        except RequestError as re:
            raise BusinessError("Error finding all time entries") from re