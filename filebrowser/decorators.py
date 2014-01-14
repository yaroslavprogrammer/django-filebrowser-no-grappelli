# coding: utf-8

import os

# DJANGO IMPORTS
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

# FILEBROWSER IMPORTS
from filebrowser.functions import get_path, get_file, convert_filename
from filebrowser.templatetags.fb_tags import query_helper


def path_exists(site, function):
    """
    Check if the given path exists.
    """

    def decorator(request, *args, **kwargs):
        if get_path('', site=site) == None:
            # The DIRECTORY does not exist, raise an error to prevent eternal redirecting.
            raise ImproperlyConfigured, _("Error finding Upload-Folder (MEDIA_ROOT + DIRECTORY). Maybe it does not exist?")
        path = request.GET.get('dir', '')
        if get_path(path, site=site) == None:
            subdir = request.GET.get('subdir', '')
            try:
                if subdir == "1":
                    path = convert_filename(path)
                    path = u'%s' % os.path.join(site.directory, path)
                    if not site.storage.isdir(path):
                        site.storage.makedirs(path)
                        return function(request, *args, **kwargs)
            except OSError, (errno, strerror):
                pass
            msg = _('The requested Folder does not exist.')
            messages.add_message(request, messages.ERROR, msg)
            redirect_url = reverse("filebrowser:fb_browse", current_app=site.name) + query_helper(request.GET, "", "dir")
            return HttpResponseRedirect(redirect_url)
        return function(request, *args, **kwargs)
    return decorator


def file_exists(site, function):
    """
    Check if the given file exists.
    """

    def decorator(request, *args, **kwargs):
        file_path = get_file(request.GET.get('dir', ''), request.GET.get('filename', ''), site=site)
        if file_path == None:
            msg = _('The requested File does not exist.')
            messages.add_message(request, messages.ERROR, msg)
            redirect_url = reverse("filebrowser:fb_browse", current_app=site.name) + query_helper(request.GET, "", "dir")
            return HttpResponseRedirect(redirect_url)
        elif file_path.startswith('/') or file_path.startswith('..'):
            # prevent path traversal
            msg = _('You do not have permission to access this file!')
            messages.add_message(request, messages.ERROR, msg)
            redirect_url = reverse("filebrowser:fb_browse", current_app=site.name) + query_helper(request.GET, "", "dir")
            return HttpResponseRedirect(redirect_url)
        return function(request, *args, **kwargs)
    return decorator


