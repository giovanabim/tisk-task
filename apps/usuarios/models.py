from django.db import models

# classes que permitem a autenticacao do login do usuario
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import check_password

class UsuarioManager(BaseUserManager):
    # Método obrigatório para criar um usuário. 
    def create_user(self, email, nome, senha=None):
        if not email:
            raise ValueError('Usuários devem ter um endereço de email válido')
        
        usuario = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )
        usuario.set_password(senha) 
        usuario.save(using=self._db)
        return usuario

    # Método obrigatório para criar superusuário
    def create_superuser(self, email, nome, senha=None):
        usuario = self.create_user(
            email,
            nome=nome,
            senha=senha,
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario
    def get_by_natural_key(self, username):
        # O username aqui será o email passado pelo authenticate
        return self.get(email=username)

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True