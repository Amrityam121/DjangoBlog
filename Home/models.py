from django.db import models

# Create your models here.


class contact(models.Model):
      Name = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      phone = models.CharField(max_length=20)
      message = models.CharField(max_length=100)
      timestamp = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return 'Message from  ' +  self.Name + '-'+ self.email

