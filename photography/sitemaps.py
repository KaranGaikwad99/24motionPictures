from django.contrib.sitemaps import Sitemap
from .models import Album

class AlbumSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
       return Album.objects.all(isActive=True)
 
    def lastmod(self, item): 
       return item.modifiedDate