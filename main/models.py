from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_("name"), max_length=250, blank=False)
    email = models.EmailField(_("email"), max_length=250, blank=False)
    subject = models.CharField(_("message"), max_length=250, blank=False)

    def __str__(self):
        return f'{self.name} : {self.subject}'
