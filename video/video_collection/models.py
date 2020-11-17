from django.db import models
from urllib import parse
from django.core.exceptions import ValidationError

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    video_id = models.CharField(max_length=40, unique=True)
    
    # overrides inherited save method
    def save(self, *args, **kwargs):
        # check for valid YT url and extract video id
        # don't save if not valid
        try:
            url_components = parse.urlparse(self.url)
            
            # check for valid URL
            invalid_scheme = url_components.scheme != 'https'
            invalid_netloc = url_components.netloc != 'www.youtube.com'
            invalid_path = url_components.path != '/watch'
            if invalid_scheme or invalid_netloc or invalid_path:
                raise ValidationError(f'Invalid YouTube URL {self.url}')
            
            query_string = url_components.query
            if not query_string:    # check that there is a query
                raise ValidationError(f'Invalid YouTube URL {self.url}')
            
            parameters = parse.parse_qs(query_string, strict_parsing=True)
            parameter_list = parameters.get('v')
            if not parameter_list:  # check that there is a video id
                raise ValidationError(f'Invalid YouTube parameters {self.url}')
            
            self.video_id = parameter_list[0]
            
        except ValueError as e:
            raise ValidationError(f'Couldn\'t parse URL {self.url}') from e
        
        # save to db
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.pk} -- {self.name} -- {self.url} -- {self.notes[:200]}'
