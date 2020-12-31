from django.db import models


class Tree(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
