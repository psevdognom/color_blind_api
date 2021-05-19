from tortoise.models import Model
from tortoise import fields, Tortoise, run_async

class UpdatedPhoto(Model):
    link = fields.CharField(max_length=30, null=True, blank=True)

