from django.db import models


class Weather(models.Model):
    temp_in = models.DecimalField('Temp in', max_digits=3, decimal_places=1)
    temp_out = models.DecimalField('Temp out', max_digits=3, decimal_places=1)
    temp_water = models.DecimalField('Temp water', max_digits=3, decimal_places=1)
    pressure = models.PositiveSmallIntegerField('Pressure')
    humidity_in = models.PositiveSmallIntegerField('Humidity in')
    humidity_out = models.PositiveSmallIntegerField('Humidity out')
    voltage = models.DecimalField('Voltage', max_digits=4, decimal_places=2)
    time = models.DateTimeField('Time', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'

    def __str__(self):
        return "{}".format(self.time)
