from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django import forms
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


from django.db import models
#from django.contrib import admin
#from my_awesome_app.models import MyAwesomeModelWithFiles


class ContentTypeRestrictedFileField(models.FileField):

    def __init__(self, content_types=None,max_upload_size=859832320, **kwargs):
        self.content_types = kwargs.pop('video/avi' , 'video/mp4')
        self.max_upload_size = max_upload_size

        super(ContentTypeRestrictedFileField, self).__init__(**kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass

        return data


class Video(models.Model):
    titol = models.CharField(max_length=100 , blank=False,unique=True,help_text="Titul del video.")
    tamany = models.IntegerField(help_text="Tamany del video.")
    tipus = models.CharField(max_length=5,blank=False)
    data = models.DateField(auto_now_add=True, help_text="Data del video pujat.")
    video = models.FileField(upload_to='.',help_text="Video per pujar",blank=False )
    usuari = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.titol)
