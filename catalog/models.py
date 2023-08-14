from django.db import models

NULL_BLANK = {'null': True, 'blank': True}


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='First Name')
    surname = models.CharField(max_length=100, verbose_name='Last Name')
    avatar = models.ImageField(upload_to='students/', verbose_name='Avatar', **NULL_BLANK,)
    age = models.PositiveSmallIntegerField(verbose_name='Age', **NULL_BLANK,)

    is_active = models.BooleanField(default=True, verbose_name='studies now',)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ('surname',)
