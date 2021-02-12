from contextlib import suppress

import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Update(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            user_id = self.user.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{user_id}",
                                    json=self.user.__dict__,
                                    headers={"Content-Type": "application/json"}
                                    ).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user by id: {user_id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.user.__dict__["_links"]["self"]
        with suppress(KeyError): del self.user.__dict__["_links"]["memberships"]
        with suppress(KeyError): del self.user.__dict__["id"]
        with suppress(KeyError): del self.user.__dict__["createdAt"]
        with suppress(KeyError): del self.user.__dict__["updatedAt"]
        with suppress(KeyError): del self.user.__dict__["name"]
        with suppress(KeyError): del self.user.__dict__["avatar"]
        with suppress(KeyError): del self.user.__dict__["status"]
        with suppress(KeyError): del self.user.__dict__["identity_url"]
