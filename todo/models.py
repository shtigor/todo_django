from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'task_list'
