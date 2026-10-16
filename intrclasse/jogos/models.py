from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=50,unique=True)
    coletiva = 'C'
    individual = 'I'
    tipo_choices = {coletiva:"coletiva", individual:"Individual"}
    tipo = models.CharField(max_length=1, choices=tipo_choices)
    max_atletas = models.PositiveIntegerField()
    def __str__(self):
            return self.nome
    class Meta:
             ordering = ['nome']

class Equipe(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    curso = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    criada_em = models.DateTimeField( auto_now_add=True)
   
    def __str__(self):
            return self.nome
    class Meta:
             ordering = ['nome']

class Tecnico(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name = 'tecnico')
    def __str__(self):
        return self.nome


class Atleta(models.Model):
    nome = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name='atletas')
    modalidades = models.ManyToManyField(Modalidade, related_name='atletas', null=True, blank=True)

    def __str__(self):
        return self.nome
    class Meta:
         ordering = ['nome']