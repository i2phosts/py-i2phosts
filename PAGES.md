How to create/customize custom pages
====================================

Previously pages like /contacts/ and / was just a templates. To change its content service operator was supposed to
edit templates directly. This is not a convenient way so it was changed.

Now, to have a page like /contacts/ be filled, you need to create/edit it via django admin interface (/admin/pages/).
Note that you should use markdown syntax here.

Index page
----------

To fill index page you need to create a page named 'index' in django admin.
Generally whether you need to obtain a page name to create, look for urls.py for 'name' kwarg to 'url()'
