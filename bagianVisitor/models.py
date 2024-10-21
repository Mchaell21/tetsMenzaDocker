from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    contactName = models.CharField(null= True,blank=True, max_length=200)
    contactEmail = models.CharField(null= True,blank=True, max_length=100)
    contactPhone = models.CharField(null= True,blank=True, max_length=100)
    contactNote = models.TextField(null=True, blank=True)

    idContact = models.CharField(null= True,blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dateCreated = models.DateTimeField(default=timezone.now,blank=True, null=True)
    lastUpdate = models.DateTimeField(default=timezone.now,blank=True, null=True)

    def __str__(self) -> str:
        return slugify('{} {}'.format(self.contactName, self.idContact))
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.dateCreated is None:
            self.dateCreated = timezone.localtime(timezone.now())
        if self.idContact is None:
            self.idContact = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.contactName, self.idContact)) 
        
        self.slug = slugify('{} {}'.format(self.contactName, self.idContact))
        self.lastUpdate = timezone.localtime(timezone.now())

        super(Contact, self).save(*args, **kwargs)