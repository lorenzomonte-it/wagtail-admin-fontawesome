Add [Fontawesome5](https://fontawesome.com/) to your Wagtail project's admin.

## Install

```
pip install wagtail-admin-fontawesome
```

than add `wagtailadminfontawesome` to your installed apps.

## Usage

#### ModelAdmin

Use icons on ModelAdmin menu, just set `menu_icon` with your favorite free icon (solid or brand) of [Fontawesome list](https://fontawesome.com/icons?d=gallery&p=2)

```
class ModelPageAdmin(ModelAdmin):
    ...
    menu_icon = 'fa-rocket'
    ...
```
