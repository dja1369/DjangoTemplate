
from mongoengine import Document, StringField, IntField


# Create your models here.
class TestModel(Document):
    name = StringField(max_length=100)
    age = IntField()

    meta = {'collection': 'test_model'}
