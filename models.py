from tortoise.models import Model
from tortoise import fields, Tortoise, run_async

class UpdatedPhoto(Model):
    link = fields.CharField(max_length=30, null=True, blank=True)
    created_time = fields.DatetimeField(auto_now=True, auto_now_add=True)
    download_count = fields.IntField()

