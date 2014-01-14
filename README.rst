Django FileBrowser
==================

**Media-Management for Django 1.4-1.6**. (based on https://github.com/sehmaschine/django-filebrowser)

The FileBrowser is an extension to the `Django <http://www.djangoproject.com>`_ administration interface in order to:

* browse directories on your server and upload/delete/edit/rename files.
* include images/documents to your models/database using the ``FileBrowseField``.
* select images/documents with TinyMCE.

Requirements
------------

FileBrowser 3.4.3 requires

* Django 1.4,1.5,1.6 (http://www.djangoproject.com)
* PIL (http://www.pythonware.com/products/pil/)

Now supports
* django-admin-sortable
* inlines (stacked, tabular) in my django fork
* supports creating dirs on-the fly on inlines and models ``get_file_path``

No Grapelli
-----------

This fork removes the dependency on Grappeli.

Installation
------------

    pip install -e git+git://github.com/yaroslav0rudenok/django-filebrowser-no-grappelli-django15.git#egg=django-filebrowser

Documentation
-------------

http://readthedocs.org/docs/django-filebrowser/

Translation
-----------

https://www.transifex.net/projects/p/django-filebrowser/
