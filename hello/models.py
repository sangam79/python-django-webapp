from django.db import models


class College(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.CharField(max_length = 20, default='0000000')
    batch = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    address = models.CharField(max_length = 200, default='0000000')
    parentsname = models.CharField(max_length = 100, default='0000000')


    class Meta:
        verbose_name_plural = "hello"

    def __str__(self):
        return self.name
