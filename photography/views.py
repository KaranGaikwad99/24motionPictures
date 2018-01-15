from django.contrib.sitemaps import Sitemap
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from .models import Album, AlbumImage

from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

def gallary(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'gallary.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album
     template_name= "album_detail.html"
     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

class AlbumSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
       return Album.objects.all(isActive=True)
 
    def lastmod(self, item): 
       return item.modifiedDate