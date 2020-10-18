from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=10,default='#F79F79')

    def __str__(self):
        return self.title

class Todo(models.Model):
    text		= models.CharField(max_length=40)
    complete	= models.BooleanField(default=False)
    created		= models.DateTimeField(auto_now_add=True)
    updated	= models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
    	return '%s %s' % (self.text,self.created)

    def get_time_elapsed(self):
        self.save()
        time = str(self.updated - self.created)
        if time[0] == '0':
            time = time[2:]
            time = time.replace(':','m:')
            time = time.replace('.','s')
            time = time[:-6]
        else:
            time = time.replace(':','m:')
            time = time.replace('.','s.')
            time = time[:-6]
        return '%s' % (time)
        

