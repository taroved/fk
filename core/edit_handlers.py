from itertools import product, chain
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.wagtailadmin.edit_handlers import EditHandler, extract_panel_definitions_from_model_class, MultiFieldPanel, \
    BaseCompositeEditHandler, get_form_for_model, ObjectList, FieldPanel
from django import forms
from wagtail.wagtailadmin.views.pages import PAGE_EDIT_HANDLERS


class TranslatableBaseTabbedInterface(BaseCompositeEditHandler):
    template = "wagtailadmin/edit_handlers/tabbed_interface.html"

    @classmethod
    def get_form_class(cls, model):
        if cls._form_class is None:
            cls._form_class = get_form_for_model(
                model,
                formsets=cls.required_formsets(), widgets=cls.widget_overrides())
        return cls._form_class


def TranslatableTabbedInterface(children):
    # children = [ObjectList(model.content_panels, heading='Content')] + \
    #            [ObjectList(getattr(model, lang+'_panels'), heading=lang) for lang in languages] + \
    #            [ObjectList(model.promote_panels, heading='Promote'),
    #             ObjectList(model.settings_panels, heading='Settings', classname="settings")]
    return type(str('_TranslatableTabbedInterface'), (TranslatableBaseTabbedInterface,),
                {'children': children})


def register_translatable_interface(model_class, fields, languages):
    # we should clone content_panels for every language but use only `fields`
    def find_panel(field):
        return next(panel for panel in model_class.content_panels if panel.field_name == field)

    def copy_panel(panel, lang):
        return FieldPanel("%s_%s" % (panel.field_name, lang), panel.classname)

    def lang_tab(lang):
        return ObjectList([copy_panel(find_panel(field), lang) for field in fields], lang)

    lang_tabs = map(lang_tab, languages)

    PAGE_EDIT_HANDLERS[model_class] = TranslatableTabbedInterface(
        [ObjectList(model_class.content_panels, heading='Content')] +
        lang_tabs +
        [ObjectList(model_class.promote_panels, heading='Promote'),
        ObjectList(model_class.settings_panels, heading='Settings', classname="settings")]
    )


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