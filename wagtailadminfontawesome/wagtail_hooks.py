from django.utils.html import format_html

from django.templatetags.static import static

from wagtail.core import hooks


def import_wagtailfontawesome_stylesheet():
    return format_html('<link rel="stylesheet" href="{}">', static('wagtailadminfontawesome/css/wagtail-admin-fontawesome.min.css'))


admin_stylesheet_hook = 'insert_global_admin_css'

hooks.register(admin_stylesheet_hook, import_wagtailfontawesome_stylesheet)
