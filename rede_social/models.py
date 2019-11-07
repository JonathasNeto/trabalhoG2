from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name="usuario",on_delete=models.CASCADE)
    nome = models.CharField( max_length = 150)
    amigos = models.ManyToManyField("Perfil", related_name="Amigos",blank=True, null=True)
    foto = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.usuario.username


class Publicao(models.Model):    
    pessoa = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)
    conteudo = models.TextField('Conteúdo',max_length = 200)
    data = models.DateTimeField(auto_now_add=True)

    def reveso(self):
        return reverse("Publicacao", kwargs={"Publicao": self.pk})

    def __str__(self):
        return self.pessoa.username

class Comentario(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    pessoa = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)
    comentario = models.ForeignKey(Publicao, on_delete=models.CASCADE, blank=True, null=True)
    resposta = models.TextField()

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios" 