import warnings
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

OLD_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', False)
if OLD_CONFIG:
    warnings.warn("TINYMCE_DEFAULT_CONFIG is deprecated, check docs for instructions.", DeprecationWarning)
DEFAULT_CONFIG = OLD_CONFIG or {'theme': "modern", 'relative_urls': False}

OLD_ADMIN_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_ADMIN_CONFIG', False)
if OLD_ADMIN_CONFIG:
    warnings.warn("TINYMCE_DEFAULT_ADMIN_CONFIG is deprecated, check docs for instructions.", DeprecationWarning)
DEFAULT_ADMIN_CONFIG = OLD_ADMIN_CONFIG or DEFAULT_CONFIG

if getattr(settings, 'TINYMCE_JS_URL', False):
    raise RuntimeError("TINYMCE_JS_URL is not supported anymore, check docs for instructions.")
JS_URL = staticfiles_storage.url('tinymce/tinymce.min.js')
JS_ROOT = staticfiles_storage.url('tinymce')
JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]

if getattr(settings, 'TINYMCE_SPELLCHECKER', False):
    raise NotImplementedError("TINYMCE_SPELLCHECKER is not implemented yet.")
USE_SPELLCHECKER = False

if getattr(settings, 'TINYMCE_COMPRESSOR', False):
    raise NotImplementedError("TINYMCE_COMPRESSOR is not implemented yet.")
USE_COMPRESSOR = False

if getattr(settings, 'TINYMCE_FILEBROWSER', False):
    raise RuntimeError("TINYMCE_FILEBROWSER is not supported anymore, check docs for instructions.")
USE_FILEBROWSER = False

CLEAN_HTML = getattr(settings, 'TINYMCE_CLEAN_HTML', False)

#CLEAN_HTML = {
    #'scripts': False,
    #'javascript': False,
    #'comments': False,
    #'style': False,
    #'links': False,
    #'meta': False,
    #'page_structure': False,
    #'processing_instructions': False,
    #'embedded': False,
    #'frames': False,
    #'forms': False,
    #'annoying_tags': False,
    #'remove_unknown_tags': False,
    #'safe_attrs_only': False}
