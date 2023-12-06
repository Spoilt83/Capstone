from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(6) 
    BookingDate = models.DateTimeField()
    
    
    class Meta:
        indexes = [models.Index(fields=['ID']),]
        
    def __str__(self):
        return f'{self.Name}'
    
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    
    class Meta:
        indexes = [models.Index(fields=['Price']),]
        
    def __str__(self):
        return f'{self.Title} : {self.Price}'
