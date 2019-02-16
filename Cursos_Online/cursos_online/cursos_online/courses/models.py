from django.db import models

class CourseManager(models.Manager):                                                        # Herança sobre models.Manager para customizar o Manager
    def search(self, query):                                                                # Customização da queryset do Manager com filtros. Condição é: ou um ou outro
        return self.get_queryset().filter(models.Q(name__icontains=query) |
                                          models.Q(description__icontains=query)
                                          )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Image',
                              null=True, blank=True)                                        # Foi criado uma variável em settings para o diretório de imagens do projeto

    created_at = models.DateTimeField('Criado em', auto_now_add=True)                       # Grava data de criação
    update_at = models.DateTimeField('Atualizado em', auto_now=True)                        # Grava data de atualização

    objects = CourseManager()                                                               # Instancia um Manager customizado que tem métodos para manipulação do banco de dados