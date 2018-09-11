from django.db import models

# Create your models here.


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(blank=False, null=False)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
