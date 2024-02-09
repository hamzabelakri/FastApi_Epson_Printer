from config.log_config import logger
from mongoengine import connect, Document, StringField, IntField, DoesNotExist, errors, DynamicDocument
from datetime import datetime


def init():
    # class User(DynamicDocument):
    #     name = StringField(required=True)
    #     age = IntField()
    #     created_at = StringField(default=str(datetime.now()))

    #     def __repr__(self):
    #         return f'name:{self.name} age:{self.age}'
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    # user_data = {'name': 'John Doe', 'age': 25, 'fisrname': 'zvo'}
    # U1 = User(name='1', test='dsdsdsd')
    # U1.tags = ['tag1', 'testtag']
    # U1.XXXX = [{'a': 1, 'b': 2}, {'a': 3, 'b': 6}]
    # U1.save()
    # young_users = User.objects(name='1')
    # print(young_users)
    # # M1.add_document(User, U1)
