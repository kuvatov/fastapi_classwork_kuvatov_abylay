from tortoise import fields

from app.db.models.base import BaseModel


class Person(BaseModel):
    fullname = fields.CharField(max_length=255, null=True)
    birth_date = fields.DateField(null=True)

    def __str__(self) -> str:
        return self.fullname
    
    class Meta(BaseModel.Meta):
        table = 'person'
        