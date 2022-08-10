from django.db import models

class SwimPlace(models.Model):
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
    
    mapotic_id = models.IntegerField()
    longitude = models.FloatField(min_value=-180,
                                  max_value=180)
    latitude = models.FloatField(min_value=-90, 
                                 max_value=90)
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    rating = models.FloatField()
    image_url = models.URLField()
    import_id = models.CharField(max_length=20)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    address = models.CharField(max_length=200, 
                               default=None)
    web = models.URLField()
    e_mail = models.EmailField()
    phone_number = models.CharField(max_length=15)
    refreshment = models.CharField(choices=REFRESH,      
                                   max_length=50)
    diving = models.CharField(choices=DIVING,
                              max_length=50)
    entrance = models.CharField(choices=ENTRANCE,
                                max_length=20)
    parking = models.CharField(max_length=50)
    link = models.URLField()
    nudist_beach = models.CharField(choices=NUDE,
                                    max_length=30)
    video = models.URLField()
    dog_swimming = models.CharField(choices=DOGS,
                                    max_length=30)
