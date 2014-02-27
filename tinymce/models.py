# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from tinymce import widgets as tinymce_widgets
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^tinymce\.models\.HTMLField'])
except ImportError:
    pass

import tinymce.settings


class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """
    def formfield(self, **kwargs):
        defaults = {'widget': tinymce_widgets.TinyMCE}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE

        return super(HTMLField, self).formfield(**defaults)

    def clean(self, *args, **kwargs):
        cleaned_data = super(HTMLField, self).clean(*args, **kwargs)
        if tinymce.settings.CLEAN_HTML:
            cleaned_data = self.clean_html(cleaned_data)
        return cleaned_data

    def clean_html(self, html, prefix="<html><body>", sufix="</body></html>"):
        from lxml.html.clean import Cleaner
        if not html:
            return ""
        cleaner = Cleaner(**tinymce.settings.CLEAN_HTML)
        # clean_html expect a parent node
        cleaned_html = cleaner.clean_html(prefix + html + sufix)
        # Remove the <html><body>
        return cleaned_html[len(prefix): len(cleaned_html) - len(sufix)]
