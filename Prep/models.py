from django.db import models

class Starter (models.Model):
    Topic = models.CharField(max_length=50)
    Sub_topic = models.CharField(max_length=200)
    Description = models.TextField()


    def __str__(self):
        return f"{self.Topic} \n {self.Sub_topic}, \n {self.Description}"
