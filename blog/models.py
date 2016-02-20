from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    pub_date = models.DateTimeField('创建时间',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['-pub_date']

class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    tags = models.CharField('标签',max_length=200,blank=True,null=True)
    summary = models.TextField('摘要',default='')
    content = models.TextField(default='',blank=True)
    pub_date = models.DateTimeField('发布时间',auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-pub_date']

