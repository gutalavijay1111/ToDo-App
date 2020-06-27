from django.db import models

class Todo(models.Model):
    text		= models.CharField(max_length=40)
    complete	= models.BooleanField(default=False)
    created		= models.DateTimeField(auto_now_add=True)
    updated	= models.DateTimeField(auto_now=True)


    def __str__(self):
    	return '%s %s' % (self.text,self.created)

    def get_time_elapsed(self):
    	self.save()
    	return '%s' % (self.updated - self.created)