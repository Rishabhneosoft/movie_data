from django.db import models

# Create your models here.
# 1. id
# 2. name
# 3. release_date
# 4. actors
# 5. poster_image
# 6. genres


# Action.
# Comedy.
# Drama.
# Fantasy.
# Horror.
# Mystery.
# Romance.
# Thriller.
STATE_CHOICE=((
    ('Action','Action'),
    ('Comedy','Comedy'),
    ('Drama','Drama'),
    ('Mystery','Mystery'),
    ('Horror','Horror'),
    ('Thriller','Thriller'),


))

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    actor = models.CharField(max_length=100)
    poster_image = models.ImageField()
    genres = models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str__(self):
        return f'{self.name}'

# isPaid = models.DateTimeField(auto_now_add=False, default=False)