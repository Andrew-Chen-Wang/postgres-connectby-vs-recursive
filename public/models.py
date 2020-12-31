from django.db import models


class Tree(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)


class ASD1(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey(Tree, on_delete=models.CASCADE)


class ASD2(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey(ASD1, on_delete=models.CASCADE)
