from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    # slug = models.SlugField('Slug', unique=True,help_text='one word for title alias')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    content = models.TextField('Desciprtion')
    create_at = models.DateTimeField('create date',auto_now_add=True, blank=False , null=False)
    update_at = models.DateTimeField('create date',auto_now=True, blank=False , null=False)

    class Meta:
        ordering = ['create_at']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:40]
    
