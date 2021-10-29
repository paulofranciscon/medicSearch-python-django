from django.db import models
from django.contrib.auth.models import user
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = {
    (1, 'Admin'),
    (2, 'Medico'),
    (3, 'Paciente')
}
#Toda vez que criar uma model e quiser que ela seja uma table em nosso database, necessário importa-lá no arquivo __init__.py
from .Profile import Profile