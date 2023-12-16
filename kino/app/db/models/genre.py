from tortoise import fields

from app.db.models.base import BaseModel


class Genre(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta(BaseModel.Meta):
        table = 'genre'
