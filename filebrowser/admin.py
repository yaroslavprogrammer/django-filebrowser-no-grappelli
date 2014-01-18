from django.contrib import admin
from django.contrib.admin.util import unquote

from .fields import FileBrowseField
from .functions import convert_filename


def set_path_for_model_fields(model, obj):
    if hasattr(model, 'get_file_path'):
        path = unicode(model.get_file_path(obj))
        path = convert_filename(path)
        for field in model._meta.fields:
            if issubclass(type(field), FileBrowseField):
                field.subdirectory = path

class FileBrowserMakeDirAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, unquote(object_id))
        for inline in self.inlines:
            set_path_for_model_fields(inline.model, obj)
        set_path_for_model_fields(self.model, obj)
        return super(FileBrowserMakeDirAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)
