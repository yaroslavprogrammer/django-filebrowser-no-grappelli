from django.contrib import admin
from django.contrib.admin.util import unquote

from .fields import FileBrowseField
from .functions import convert_filename


def get_path_for_object_id(object_id):
    obj = self.get_object(request, unquote(object_id))
    path = unicode(inline.model.get_file_path(obj))
    path = convert_filename(path)
    return path

def set_path_for_model_fields(model, object_id):
    if hasattr(model, 'get_file_path'):
        path = get_path_for_object_id(object_id)
        for field in model._meta.fields:
            if issubclass(type(field), FileBrowseField):
                field.subdirectory = path

class FileBrowserMakeDirAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        for inline in self.inlines:
            set_path_for_model_fields(inline.model, object_id)
        set_path_for_model_fields(self.model, object_id)
        return super(FileBrowserMakeDirAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)
