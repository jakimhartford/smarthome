from django.db import models

# Create your models here.


class BulbType(models.Model):
    buld_type_id = models.AutoField(primary_key=True)
    bulb_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bulb_type_name


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.romm_name

class Bulb(models.Model):
    bulb_id = models.AutoField(primary_key=True)
    bulb_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, null=True,blank=True)
    bulb_type = models.ForeignKey(BulbType, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.bulb_name
