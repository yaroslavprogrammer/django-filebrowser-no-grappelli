from django.contrib import admin
from django.contrib.admin.util import unquote

from .fields import FileBrowseField


class FileBrowserMakeDirAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        for inline in self.inlines:
            if hasattr(inline.model, 'get_file_path'):
                obj = self.get_object(request, unquote(object_id))
                path = unicode(inline.model.get_file_path(obj))
                for field in inline.model._meta.fields:
                    if issubclass(type(field), FileBrowseField):
                        field.subdirectory = path
        if hasattr(self.model, 'get_file_path'):
            for field in self.model._meta.fields:
                if issubclass(type(field), FileBrowseField):
                    field.subdirectory = path
        return super(FileBrowserMakeDirAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)
