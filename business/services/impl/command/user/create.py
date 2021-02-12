import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Create(UserCommand):

    def __init__(self, connection, login, email, first_name, last_name, admin, language, status, password):
        super().__init__(connection)
        self.user = {
            "login": login,
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "admin": admin,
            "language": language,
            "status": status,
            "password": password
        }

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.user).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating new user") from re
