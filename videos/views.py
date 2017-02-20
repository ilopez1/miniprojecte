from django.shortcuts import render , get_object_or_404 , redirect
from videos.models import Video
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse



@login_required
def llista_videos(request):
    videos = (Video.objects.order_by("nom"))
    paginacion = Paginator(videos, 30)
    page = request.GET.get('page')


    try:
        videos = paginacion.page(page)
    except PageNotAnInteger:
        videos = paginacion.page(1)
    except EmptyPage:
        videos = paginacion.page(paginacion.num_pages)
    ctx = {
        'videos': videos
    }

    return render(request, 'llista_videos.html', ctx)



class Home( generic.TemplateView ):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super( Home, self ).get_context_data( **kwargs )
        context['accepted_mime_types'] = ['image/*']
        return context

@require_POST
def upload( request ):
    video = upload_receive( request )

    instance = Video( video = video )
    instance.save()

    basename = os.path.basename( instance.video.path )
    
    file_dict = {
        'name' : basename,
        'size' : video.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnailUrl': settings.MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, pk ):
    success = True
    try:
        instance = Video.objects.get( pk = pk )
        os.unlink( instance.video.path )
        instance.delete()
    except Video.DoesNotExist:
        success = False

    return JFUResponse( request, success )
 