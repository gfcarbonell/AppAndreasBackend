# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
import datetime
from rates.models import Rate 
from auth_users.models import AuthUser 

# Create your models here.
class Task(models.Model):
    '''
        This class:<Rates> contains the user information.
        Esta class:<Tarifa> contiene la información de las tarifas por lote.
    '''
    user = models.ForeignKey(
        AuthUser,
        db_index=True,
        on_delete=models.CASCADE,
        help_text='Menu | Menú'
    )
    rate = models.ForeignKey(
        Rate,
        db_index=True,
        on_delete=models.CASCADE,
        help_text='Menu | Menú'
    )
    active = models.BooleanField(
        default=True,
        help_text='Active | Activo',
    )
    slug = models.SlugField(
        editable=False, 
        max_length=255,
        unique=True, 
        db_index=True 
    )
    
    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.get_name())
        else:
            slug = slugify(self.get_name())
            if self.slug != slug:
                self.slug = slug
        super(Task, self).save(*args, **kwargs)

    def get_name(self):
        return '%s - %s - %s' %(self.user.username, self.rate.get_name(), self.scheduled_date)

    class Meta:
        db_table = 'task'
        ordering = ('user', 'rate')
        verbose_name = 'Task'
        verbose_name_plural = 'Task'