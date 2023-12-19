from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Redirect(models.Model):
    key = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key + ' - ' + self.url
    

@receiver(post_save, sender=Redirect)
def redirect_post_save(sender, instance, created, **kwargs):
    if created:
        # print(**kwargs)
        # if active:
        #     cache.set("my_key", "hello, world!", 30)
        #     print("Cacheado")
        #     # Se ejecuta solo cuando se crea una nueva instancia de Redirect
        print(f'Nueva instancia de Redirect creada con la clave: {instance.key}')
     