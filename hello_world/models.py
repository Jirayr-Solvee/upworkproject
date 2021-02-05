from django.db import models

class SecondTable(models.Model):
    some_text = models.TextField()

    def __str__(self):
        return self.some_text

class FirstTable(models.Model):
    some_text = models.TextField()
    second_table = models.ForeignKey(SecondTable, related_name='second_table', on_delete=models.CASCADE)

    def __str__(self):
        return self.some_text
