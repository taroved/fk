from wagtail.wagtailcore import hooks


# @hooks.register('insert_editor_js')
# def editor_js():
#   js_files = [
#         'demo/js/hallo-plugins/hallo-demo-plugin.js',
#   ]
#   js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
#     ((settings.STATIC_URL, filename) for filename in js_files)
#   )
#   return js_includes + format_html(
#     """
#     <script>
#       registerHalloPlugin('demoeditor');
#     </script>
#     """
#   )