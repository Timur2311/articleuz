# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models




# MALE = "Erkak"
# FEMALE = "Ayol"
# GENDER_CHOICES = (
#     (MALE, "Erkak"),
#     (FEMALE, "Ayol")
# )




class User(AbstractUser):
    full_name = models.CharField(("full name"), max_length=256, null=True, blank=True)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        }, null=True, blank=True
    )
    
    phone_number = models.CharField(max_length=50, null=True, blank=True)  
    
    following = models.ManyToManyField('self')
    
    facebook_link = models.CharField(max_length=128, null=True, blank=True)
    twitter_link = models.CharField(max_length=128, null=True, blank=True)
    instagram_link = models.CharField(max_length=128, null=True, blank=True)
    
    created_at = models.DateTimeField(("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    first_name = None
    last_name = None
    
    selected_tags = models.ManyToManyField('post.Tags', related_name="user_selected_tags")
   

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")
        
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self')
    following = models.ManyToManyField('self')
    




    
    

    
    
    
    
