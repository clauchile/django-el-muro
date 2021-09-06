from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['firstname_len'] = " El nombre debe tener al menos 2 caracteres"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Correo inválido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "El nombre debe contener unicamente letras"

        if len(postData['password']) < 8:
            errors['password'] = "La contraseña debe tener al menos 8 caracteres"

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "Contraseña y confirmar contraseña no coinciden "

        
        return errors

# author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

class Message(models.Model):
    mensaje = models.CharField(max_length=255)
    user= models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.mensaje} ({self.user})"

    # def __repr__(self):
    #     return f"{self.mensaje} ({self.user})"


class Comment(models.Model):
    comentario = models.CharField(max_length=255)
    message = models.ForeignKey(Message, related_name = "comments", on_delete = models.CASCADE)
    user= models.ForeignKey(User, related_name = "usuarios", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comentario} ({self.message})"

    def __repr__(self):
        return f"{self.comentario} ({self.message})"