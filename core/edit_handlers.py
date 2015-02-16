from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.wagtailadmin.edit_handlers import EditHandler, extract_panel_definitions_from_model_class, MultiFieldPanel
from django import forms


class BaseInlineTestPanel(EditHandler):
    @classmethod
    def get_panel_definitions(cls):
        # Look for a panels definition in the InlinePanel declaration
        if cls.panels is not None:
            return cls.panels
        # Failing that, get it from the model
        else:
            return extract_panel_definitions_from_model_class(cls.related.model, exclude=[cls.related.field.name])

    _child_edit_handler_class = None

    @classmethod
    def get_child_edit_handler_class(cls):
        if cls._child_edit_handler_class is None:
            panels = cls.get_panel_definitions()
            cls._child_edit_handler_class = MultiFieldPanel(panels, heading=cls.heading)

        return cls._child_edit_handler_class

    @classmethod
    def required_formsets(cls):
        return [cls.relation_name]

    @classmethod
    def widget_overrides(cls):
        overrides = cls.get_child_edit_handler_class().widget_overrides()
        if overrides:
            return {cls.relation_name: overrides}
        else:
            return {}

    def __init__(self, instance=None, form=None):
        super(BaseInlineTestPanel, self).__init__(instance=instance, form=form)

        self.formset = form.formsets[self.__class__.relation_name]

        child_edit_handler_class = self.__class__.get_child_edit_handler_class()
        self.children = []
        for subform in self.formset.forms:
            # override the DELETE field to have a hidden input
            subform.fields['DELETE'].widget = forms.HiddenInput()

            # ditto for the ORDER field, if present
            if self.formset.can_order:
                subform.fields['ORDER'].widget = forms.HiddenInput()

            self.children.append(
                child_edit_handler_class(instance=subform.instance, form=subform)
            )

        # if this formset is valid, it may have been re-ordered; respect that
        # in case the parent form errored and we need to re-render
        if self.formset.can_order and self.formset.is_valid():
            self.children = sorted(self.children, key=lambda x: x.form.cleaned_data['ORDER'])

        empty_form = self.formset.empty_form
        empty_form.fields['DELETE'].widget = forms.HiddenInput()
        if self.formset.can_order:
            empty_form.fields['ORDER'].widget = forms.HiddenInput()

        self.empty_child = child_edit_handler_class(instance=empty_form.instance, form=empty_form)

    template = "wagtailadmin/edit_handlers/inline_panel.html"

    def render(self):
        return mark_safe(render_to_string(self.template, {
            'self': self,
            'can_order': self.formset.can_order,
        }))

    js_template = "wagtailadmin/edit_handlers/inline_panel.js"

    def render_js(self):
        return mark_safe(render_to_string(self.js_template, {
            'self': self,
            'can_order': self.formset.can_order,
        }))


def InlineTestPanel(base_model, relation_name, panels=None, label='', help_text=''):
    rel = getattr(base_model, relation_name).related
    return type(str('_InlinePanel'), (BaseInlineTestPanel,), {
        'relation_name': relation_name,
        'related': rel,
        'panels': panels,
        'heading': label,
        'help_text': help_text,  # TODO: can we pick this out of the foreign key definition as an alternative? (with a bit of help from the inlineformset object, as we do for label/heading)
    })