from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Editor(models.Model):
    text = RichTextField()