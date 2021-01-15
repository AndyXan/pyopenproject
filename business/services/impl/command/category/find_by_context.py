from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.category.category_command import CategoryCommand
from model.category import Category

class FindByContext(CategoryCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Category(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding category by context: {self.context}") from re