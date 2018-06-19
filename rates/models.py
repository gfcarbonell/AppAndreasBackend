# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Rate(models.Model):
    '''
        This class:<Rates> contains the user information.
        Esta class:<Tarifa> contiene la información de las tarifas por lote.
    '''
    lot = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ], 
        default=0,
        help_text='Lot | Lote'
    )
    location = models.CharField(
        unique=True,
        db_index=True,
        max_length=100,
        help_text='Name | Nombre'
    )
    rate = models.DecimalField(
        max_digits=6, 
        decimal_places=3,
        help_text='Rate | Tarifa'
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description | Descripción'
    )
    observation = models.TextField(
        null=True,
        blank=True,
        help_text='Observation | Observación'
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
        super(Rate, self).save(*args, **kwargs)

    def get_name(self):
        return 'Lote: %s - %s - %f' %(self.lot, self.location, self.rate)

    class Meta:
        db_table = 'rates'
        ordering = ('lot', 'location')
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'