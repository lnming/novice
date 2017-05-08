from peewee import *

database = SqliteDatabase('haopic.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Image(BaseModel):
    author = TextField(null=True)
    date = DateField(null=True)
    title = TextField(null=True)
    uri = TextField(null=True, unique=True)

    class Meta:
        db_table = 'image'

class Tag(BaseModel):
    name = TextField(null=True, unique=True)

    class Meta:
        db_table = 'tag'

class Relationship(BaseModel):
    img = ForeignKeyField(db_column='img', null=True, rel_model=Image, to_field='id')
    tag = ForeignKeyField(db_column='tag', null=True, rel_model=Tag, to_field='id')

    class Meta:
        db_table = 'relationship'

class SqliteSequence(BaseModel):
    name = UnknownField(null=True)  # 
    seq = UnknownField(null=True)  # 

    class Meta:
        db_table = 'sqlite_sequence'

