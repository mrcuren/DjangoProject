from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    STATUS = (('True','Evet'),
            ('False','Hayır'),
            )

    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    parent= TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:

        order_insertion_by = ['title']
    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '->'.join(full_path[::-1])
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

class Course(models.Model):
    STATUS = (('True','Evet'),
            ('False','Hayır'),
            )

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    detail=RichTextUploadingField()
    price=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
class Images(models.Model):

    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title


"""
class Content(models.Model):
    STATUS = (('True','Evet'),
            ('False','Hayır'),
            )

    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    img = models.ImageField(upload_to='images_uploaded', null=True)
    file=models.FileField(null=True,blank=True)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
"""
