from django.db import models


class TableManager(models.Manager):
    def create_table(self, date, name, amount, distance):
        table = self.model(date=date, name=name, amount=amount, distance=distance)
        table.save()
        return table


class Table(models.Model):
    date = models.DateTimeField("Дата")
    name = models.CharField("Название", max_length=30)
    amount = models.IntegerField("Количество")
    distance = models.FloatField("Расстояние")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    objects = TableManager()

    class Meta:
        db_table = 'table'
