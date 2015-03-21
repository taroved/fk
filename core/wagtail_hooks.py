from django.conf import settings
from django.utils.html import format_html, escapejs, format_html_join
from django.utils.safestring import mark_safe
from wagtail.wagtailcore import hooks


# @hooks.register('insert_editor_js')
# def editor_js():
# js_files = [
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

@hooks.register('insert_editor_css')
def editor_css():
    return format_html('<link rel="stylesheet" href="' +
                       settings.STATIC_URL +
                       'css/inline_panel_customization.css">')


@hooks.register('insert_editor_js')
def editor_js():
    # dirty hack for reinitialising timepicker on several pages
    # unless not found a good way to override wagtail/page-editor.js initTimeChooser function
    return mark_safe(
        '''
        <script>
            $(function() {
                $('#id_start_time, #id_end_time').datetimepicker('destroy').datetimepicker({
                    closeOnDateSelect: true,
                    datepicker: false,
                    scrollInput:false,
                    step: 30,
                    format: 'H:i',
                    i18n: {
                        lang: window.dateTimePickerTranslations
                    },
                    lang: 'lang'
                });
            })
        </script>
        '''
    )
