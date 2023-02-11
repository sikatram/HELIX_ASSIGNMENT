from django.db import models
import logging

logger = logging.getLogger('django')

class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        logger.info("SUCCESS: Saving entry to the database")
        super().save(*args, **kwargs)
