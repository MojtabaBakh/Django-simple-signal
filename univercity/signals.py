from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
import os

@receiver( post_save , sender = Student )
def create_student(sender , instance , created , **kwargs):
     if created :
         os.mkdir(f'statics/univercity/students/{instance.Name}{instance.Family}')