# hems

This project is a work in progress. 

I am now adding the WYSIWYM editor widget for Django’s admin interface....
I am following these instructions:
  http://web.archive.org/web/20101123194618/http://jannisleidel.com/2008/11/wysiwym-editor-widget-django-admin-interface/
  
I chose to at the following code:

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            'jquery/jquery.js',
            'wymeditor/jquery.wymeditor.pack.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            jQuery('#id_%s').wymeditor({
                updateSelector: '.submit-row input[type=submit]',
                updateEvent: 'click',
                lang: '%s',
            });
            </script>''' % (name, self.language))
            
 to the widgets.py file in the: 
 
  (/hems/hems_env/lib/python2.7/site-packages/django/contrib/admin) directory.




