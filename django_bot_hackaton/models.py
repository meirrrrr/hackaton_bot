from django.db import models


class Teacher(models.Model):
    external_id = models.PositiveIntegerField(verbose_name='ID учителя',)
    first_name = models.TextField(verbose_name='Имя и фамилия учителя')

    def __str__(self):
        return f'#{self.external_id} {self.first_name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
