from django.db import models
from haversine import haversine


class SwimPlace(models.Model):
    CR_CENTER = (49.7437572, 15.3386383)     
    REFRESH = (("Restaurant on site",
                "Restaurant on site"),
               ("No restaurant",
                "No restaurant"))
    DIVING = (("Suitable for diving",
               "Suitable for diving"),
              ("Not suitable for diving",
               "Not suitable for diving"))
    ENTRANCE = (("Entrance fee",
               "Entrance fee"),
              ("No entrance fee",
               "No entrance fee"))
    NUDE = (("Suitable for nudists",
             "Suitable for nudists"),
            ("Not suitable for nudists",
             "Not suitable for nudists"))
    DOGS = (("Suitable for dogs",
            "Suitable for dogs"),
           ("Not suitable for dogs",
            "Not suitable for dogs"))
   
    id = models.IntegerField(primary_key=True) # it is Mapotic ID
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", related_name='category', on_delete=models.PROTECT, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    image_url = models.URLField()
    import_id = models.CharField(max_length=20, null=True, blank=True)
    description1 = models.CharField(max_length=200, null=True, blank=True)
    description2 = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    e_mail = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    refreshment = models.CharField(choices=REFRESH,      
                                   max_length=50, null=True, blank=True)
    diving = models.CharField(choices=DIVING,
                              max_length=50, null=True, blank=True)
    entrance = models.CharField(choices=ENTRANCE,
                                max_length=20, null=True, blank=True)
    parking = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    nudist_beach = models.CharField(choices=NUDE,
                                    max_length=30, null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    dog_swimming = models.CharField(choices=DOGS,
                                    max_length=30, null=True, blank=True)
    from_cr_center = models.FloatField(editable=False, default=None, null=True, blank=True)
    
    
    def save(self, *args, **kwarg):
        self.from_cr_center = haversine(self.CR_CENTER, (float(self.latitude), float(self.longitude)))
        super(SwimPlace, self).save(*args, **kwarg)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=160, null=True, blank=True)
    swimplace = models.ForeignKey(SwimPlace, related_name='comments', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.text

class Temperature(models.Model):
    degree = models.FloatField(null=True, blank=True, default="Not available")
    update_time = models.DateTimeField(auto_now=True)
    swimplace = models.OneToOneField(SwimPlace, related_name='temperature', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.swimplace.name
