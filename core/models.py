# coding=utf-8
from datetime import date
from datetime import datetime
import string
import urlparse
from django.core.cache import cache
from django.db.models.fields import Field
from django.utils import translation
from django.utils.encoding import smart_text
import re

from django.conf.urls import url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.shortcuts import render_to_response, redirect
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from django.utils.translation import ugettext_lazy as _, ugettext_lazy
import six
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, PageChooserPanel, \
    FieldRowPanel, \
    ObjectList
from wagtail.wagtailadmin.views.pages import PAGE_EDIT_HANDLERS
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from core.edit_handlers import TranslatableTabbedInterface, register_translatable_interface, PageParentedChooserPanel
from core.fields import IntegerRangeField
from urlparse import urlparse
from os.path import splitext, basename

MODELS_LANGUAGES = ('ru', 'en')
DEFAULT_PAGE_SIZE = 10

LANGUAGE_CHOICES = (
    ('uk', _('Ukrainian')),
    ('ru', _('Russian')),
    ('en', _('English')),
)

BROWSABLE_PAGE_PROMOTE_PANELS = [
    MultiFieldPanel([
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('show_in_menus'),
        FieldPanel('is_browsable'),
        FieldPanel('search_description'),
    ], ugettext_lazy('Common page configuration'))
]


def current_lang_filter_params():
    lang = translation.get_language()
    return {'language': lang}
    # return {} if lang == 'uk' else {'has_' + lang: True}


class BrowsableMixin(models.Model):
    is_browsable = models.BooleanField(default=True, help_text=_("Whether a browsable link to this page will "
                                                                 "appear in automatically generated menus"))

    class Meta:
        abstract = True


class TranslatablePage(Page):
    is_abstract = True

    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    class Meta:
        abstract = True


class BaseMaterialPage(Page):
    is_abstract = True

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_CHOICES[0][0])
    is_browsable = True

    class Meta:
        abstract = True


class AccreditationPageFormField(AbstractFormField):
    page = ParentalKey('AccreditationPage', related_name='form_fields')


class AccreditationPage(AbstractEmailForm, BrowsableMixin):

    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True, verbose_name='body')
    body_en = RichTextField(blank=True, null=True, verbose_name='body')

    thank_you_text = RichTextField(blank=True, null=True)
    thank_you_text_ru = RichTextField(blank=True, null=True, verbose_name='thank you text')
    thank_you_text_en = RichTextField(blank=True, null=True, verbose_name='thank you text')


AccreditationPage.content_panels = [
    FieldPanel('title', classname="title full"),
    FieldPanel('body', classname="full"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email"),
    MultiFieldPanel([
        InlinePanel(AccreditationPage, 'form_fields', label="Form fields"),
    ], heading='Form fields', classname="collapsible collapsed")
]

AccreditationPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

# just id's for django makemessages translations
_accreditation_page_translations = [
    _("name"),
    _("position"),
    _("publisher"),
    _("publisher_link"),
    _("mobile_phone"),
    _("work_phone"),
    _("email"),
    _("publication_form_date"),
    _("need_additional_help"),
]

register_translatable_interface(AccreditationPage, fields=('title', 'body', 'thank_you_text'),
                                languages=MODELS_LANGUAGES)


@register_snippet
class Advert(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
        ImageChooserPanel('image'),
    ]

    def __unicode__(self):
        return "%s (%s)" % (self.text, self.url)


@register_snippet
class SliderItem(models.Model):
    text = RichTextField(null=True, blank=True)
    text_ru = RichTextField(null=True, blank=True, verbose_name='text')
    text_en = RichTextField(null=True, blank=True, verbose_name='text')

    button_text = models.CharField(max_length=50, null=True, blank=True)
    button_text_ru = models.CharField(max_length=50, null=True, blank=True, verbose_name='button text')
    button_text_en = models.CharField(max_length=50, null=True, blank=True, verbose_name='button text')

    button_link = models.URLField(null=True, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('text', classname="full"),
            FieldPanel('button_text'),
            FieldPanel('button_link'),
        ], heading='Default'),

        MultiFieldPanel([
            FieldPanel('text_ru', classname="full"),
            FieldPanel('button_text_ru'),
        ], heading='RU'),

        MultiFieldPanel([
            FieldPanel('text_en', classname="full"),
            FieldPanel('button_text_en'),
        ], heading='EN'),
    ]

    def __unicode__(self):
        return strip_tags(self.text.replace(">", "> "))


@register_snippet
class Partner(models.Model):
    title = models.CharField(max_length=255, help_text=_("The title as you'd like it to be seen by the public"))
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True, verbose_name='description')
    description_en = models.TextField(null=True, blank=True, verbose_name='description')

    panels = [
        MultiFieldPanel([
            FieldPanel('title', classname="title full"),
            ImageChooserPanel('logo'),
            FieldPanel('link', classname="full link"),
            FieldPanel('description', classname="full description"),
        ], heading='Default'),

        MultiFieldPanel([
            FieldPanel('title_ru', classname="title full"),
            FieldPanel('description_ru', classname="full description"),
        ], heading='RU'),

        MultiFieldPanel([
            FieldPanel('title_en', classname="title full"),
            FieldPanel('description_en', classname="full description"),
        ], heading='EN'),
    ]

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.link)


class PhotoAlbumPage(BaseMaterialPage):
    link = models.URLField(default='')
    date = models.DateField(default=datetime.now)

    @property
    def preview_url(self):
        match = re.search("sets/(?P<id>\d+)", self.link)
        if not match:
            return ''

        album_id = match.group("id")
        preview_url = 'http://flickrit.com/slideshowholder.php?height=100&size=big&setId={0}' \
                      '&counter=true&thumbnails=2&transition=0&layoutType=responsive&sort=0&theme=1' \
            .format(album_id)
        return preview_url

    preview = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True, null=True, default='')

    subpage_types = []
    parent_page_types = ['core.MaterialsAlbumsPage']

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('language'),
        FieldPanel('date', classname="date"),
        FieldPanel('link', classname="link full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full"),
    ]


class DocumentPage(BaseMaterialPage):
    date = models.DateField(default=datetime.now)

    doc = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    preview = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True, null=True, default='')

    def extension(self):
        disassembled = urlparse(self.doc.url)
        filename, ext = splitext(basename(disassembled.path))
        return ext.upper()
        #return (filename + ext).upper()

    subpage_types = []
    parent_page_types = ['core.MaterialsDocumentsPage']

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('language'),
        FieldPanel('date', classname="date"),
        DocumentChooserPanel('doc'),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


class VideoPage(BaseMaterialPage):
    date = models.DateField(default=datetime.now)

    link = models.URLField(default='')
    code = models.TextField(default='')
    preview = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True, null=True, default='')

    subpage_types = []
    parent_page_types = ['core.MaterialsVideoPage']

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('language'),
        FieldPanel('date', classname="date"),
        FieldPanel('link', classname="full"),
        FieldPanel('code', classname="full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


class MaterialsPage(TranslatablePage, BrowsableMixin):
    @property
    def albums(self):
        return PhotoAlbumPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    @property
    def documents(self):
        return DocumentPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    @property
    def videos(self):
        return VideoPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    subpage_types = ['core.MaterialsAlbumsPage', 'core.MaterialsVideoPage', 'core.MaterialsDocumentsPage']
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(MaterialsPage, fields=('title', ), languages=MODELS_LANGUAGES)


class MaterialsAlbumsPage(TranslatablePage, BrowsableMixin):
    @property
    def albums(self):
        return PhotoAlbumPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    subpage_types = ['core.PhotoAlbumPage']
    parent_page_types = ['core.MaterialsPage']
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(MaterialsAlbumsPage, fields=('title', ), languages=MODELS_LANGUAGES)


class MaterialsVideoPage(TranslatablePage, BrowsableMixin):
    @property
    def videos(self):
        return VideoPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    subpage_types = ['core.VideoPage']
    parent_page_types = ['core.MaterialsPage']
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(MaterialsVideoPage, fields=('title', ), languages=MODELS_LANGUAGES)


class MaterialsDocumentsPage(TranslatablePage, BrowsableMixin):
    @property
    def documents(self):
        return DocumentPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())

    subpage_types = ['core.DocumentPage']
    parent_page_types = ['core.MaterialsPage']
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(MaterialsDocumentsPage, fields=('title', ), languages=MODELS_LANGUAGES)


class NewsPageVideo(Orderable):
    page = ParentalKey('core.NewsPage', related_name='videos')
    video = models.ForeignKey('core.VideoPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('video', page_type=VideoPage, parent_cls=MaterialsVideoPage)]


class NewsPagePhotoAlbum(Orderable):
    page = ParentalKey('core.NewsPage', related_name='albums')
    album = models.ForeignKey('core.PhotoAlbumPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('album', page_type=PhotoAlbumPage, parent_cls=MaterialsAlbumsPage)]


class NewsPageDocument(Orderable):
    page = ParentalKey('core.NewsPage', related_name='documents')
    doc = models.ForeignKey('core.DocumentPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('doc', page_type=DocumentPage, parent_cls=MaterialsDocumentsPage)]


class NewsPage(BaseMaterialPage):
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    date = models.DateField(default=datetime.now)

    short = models.TextField()
    body = RichTextField()
    # tags = ClusterTaggableManager(through=NewsPageTag, blank=True)

    @property
    def news_index(self):
        # Find closest ancestor which is a index
        return self.get_ancestors().type(NewsIndexPage).last()

    subpage_types = []

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('language'),
        ImageChooserPanel('image'),
        FieldPanel("date"),
        FieldPanel("short"),
        FieldPanel("body", classname="full")
    ]

NewsPage.materials_panels = [
    InlinePanel(NewsPage, 'videos', label='Videos'),
    InlinePanel(NewsPage, 'albums', label='Albums'),
    InlinePanel(NewsPage, 'documents', label='Documents'),
]

PAGE_EDIT_HANDLERS[NewsPage] = TranslatableTabbedInterface([
    ObjectList(NewsPage.content_panels, heading='Content'),
    ObjectList(NewsPage.materials_panels, heading='Materials'),
    ObjectList(NewsPage.promote_panels, heading='Promote'),
    ObjectList(NewsPage.settings_panels, heading='Settings', classname="settings")
])



class NewsIndexPage(TranslatablePage, BrowsableMixin):
    @property
    def news(self):
        # Get list of live news pages that are descendants of this page
        news = NewsPage.objects.live().descendant_of(self).filter(**current_lang_filter_params())
        # Order by most recent date first
        news = news.order_by('-date')
        return news

    def get_context(self, request, **kwargs):
        news = self.news
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(news, DEFAULT_PAGE_SIZE)  # Show 10 news per page
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        # Update template context
        context = super(NewsIndexPage, self).get_context(request)
        context['news'] = news
        return context

    subpage_types = ['core.NewsPage', 'core.PressTopPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(NewsIndexPage, fields=('title',), languages=MODELS_LANGUAGES)


class OrgPage(TranslatablePage, BrowsableMixin):
    @property
    def organizers(self):
        return OrganizerPage.objects.live().all()

    subpage_types = ['core.OrganizerPage']

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(OrgPage, fields=('title',), languages=MODELS_LANGUAGES)


class ParticipationPage(TranslatablePage, BrowsableMixin):
    pass


register_translatable_interface(ParticipationPage, fields=('title',), languages=MODELS_LANGUAGES)


class RadaMemberPage(TranslatablePage, BrowsableMixin):

    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    position = models.CharField(max_length=255, blank=True, null=True, default='')
    position_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')
    position_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')

    about = RichTextField(blank=True, null=True, default='')
    about_ru = RichTextField(blank=True, null=True, default='', verbose_name='about')
    about_en = RichTextField(blank=True, null=True, default='', verbose_name='about')

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('photo'),
        FieldPanel('position', classname="full"),
        FieldPanel('about', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    search_fields = Page.search_fields + (
        index.SearchField('title_ru', partial_match=True, boost=2),
        index.SearchField('title_en', partial_match=True, boost=2),
        index.SearchField('about', partial_match=True),
        index.SearchField('about_ru', partial_match=True),
        index.SearchField('about_en', partial_match=True),
    )

register_translatable_interface(RadaMemberPage, fields=('title', 'position', 'about'), languages=MODELS_LANGUAGES)



class RadaPage(TranslatablePage, BrowsableMixin):

    @property
    def members(self):
        return self.get_descendants().type(RadaMemberPage).live().all()

    subpage_types = ['core.RadaMemberPage']


RadaPage.content_panels = [
    FieldPanel('title', classname="full title"),
]
RadaPage.ru_panels = [
    FieldPanel('title_ru', classname="full title"),
]
RadaPage.en_panels = [
    FieldPanel('title_en', classname="full title"),
]
# RadaPage.members_panels = [
#     InlinePanel(RadaPage, 'members', label='Members'),
# ]
RadaPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

# register_translatable_interface(RadaPage, fields=('title',), languages=MODELS_LANGUAGES)

PAGE_EDIT_HANDLERS[RadaPage] = TranslatableTabbedInterface([
    ObjectList(RadaPage.content_panels, heading='Content'),
    ObjectList(RadaPage.ru_panels, heading='RU'),
    ObjectList(RadaPage.en_panels, heading='EN'),
    ObjectList(RadaPage.promote_panels, heading='Promote'),
    ObjectList(RadaPage.settings_panels, heading='Settings', classname="settings")
])



class PartnerListPage(TranslatablePage, BrowsableMixin):
    @property
    def partners(self):
        return Partner.objects.all()

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(PartnerListPage, fields=('title',), languages=MODELS_LANGUAGES)


class OrganizerPage(TranslatablePage, BrowsableMixin):
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True, verbose_name='description')
    description_en = models.TextField(blank=True, null=True, verbose_name='description')

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('link', classname="full link"),
        FieldPanel('description', classname="full description"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(OrganizerPage, fields=('title', 'description'), languages=MODELS_LANGUAGES)


class ForumIndexPage(TranslatablePage, BrowsableMixin):
    @property
    def forums(self):
        # Get list of live event pages that are descendants of this page
        forums = ForumPage.objects.live().descendant_of(self)
        # Filter events list to get ones that are either
        # running now or start in the future
        forums = forums.filter(date_from__lte=date.today())
        # Order by date
        forums = forums.order_by('date_from')
        return forums

    subpage_types = ['core.ForumPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    class Meta:
        verbose_name = 'Forum Archive Page'


register_translatable_interface(ForumIndexPage, fields=('title', ), languages=MODELS_LANGUAGES)


class MaterialVideoLinkFields(models.Model):
    video = models.ForeignKey(VideoPage,
                              null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+')

    panels = [PageChooserPanel('video', page_type=VideoPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.video.title)

    class Meta:
        abstract = True


class ForumPageVideo(Orderable, MaterialVideoLinkFields):
    page = ParentalKey('core.ForumPage', related_name='videos')


class MaterialAlbumLinkFields(models.Model):
    album = models.ForeignKey(PhotoAlbumPage,
                              null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+')

    panels = [PageChooserPanel('album', page_type=PhotoAlbumPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.album.title)

    class Meta:
        abstract = True


class ForumPagePhotoAlbum(Orderable, MaterialAlbumLinkFields):
    page = ParentalKey('core.ForumPage', related_name='albums')

class MaterialDocLinkFields(models.Model):
    doc = models.ForeignKey(DocumentPage,
                            null=True, blank=True,
                            on_delete=models.SET_NULL,
                            related_name='+')

    panels = [PageChooserPanel('doc', page_type=DocumentPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.doc.title)

    class Meta:
        abstract = True


class ForumPageDocument(Orderable, MaterialDocLinkFields):
    page = ParentalKey('core.ForumPage', related_name='documents')


class SpeakerPage(TranslatablePage, BrowsableMixin):
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    position = models.CharField(max_length=255, blank=True, null=True, default='')
    position_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')
    position_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')

    about = RichTextField(blank=True, null=True, default='')
    about_ru = RichTextField(blank=True, null=True, default='', verbose_name='about')
    about_en = RichTextField(blank=True, null=True, default='', verbose_name='about')

    parent_page_types = ['core.AllSpeakersIndexPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('photo'),
        FieldPanel('position', classname="full"),
        FieldPanel('about', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    search_fields = Page.search_fields + (
        index.SearchField('title_ru', partial_match=True, boost=2),
        index.SearchField('title_en', partial_match=True, boost=2),
        index.SearchField('about', partial_match=True),
        index.SearchField('about_ru', partial_match=True),
        index.SearchField('about_en', partial_match=True),
    )


register_translatable_interface(SpeakerPage, fields=('title', 'position', 'about'), languages=MODELS_LANGUAGES)


class AllSpeakersIndexPage(TranslatablePage, BrowsableMixin):
    def speakers(self):
        speakers = SpeakerPage.objects.live().descendant_of(self)
        return speakers

    subpage_types = ['core.SpeakerPage']

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    class Meta:
        verbose_name = 'Speaker'


register_translatable_interface(AllSpeakersIndexPage, fields=('title', ), languages=MODELS_LANGUAGES)


def guess_speaker_lastname(speaker):
    return speaker.title.split()[-1]


uk_ru_en_uppercase = list(u'АБВГҐДЕЁЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ') + list(string.ascii_uppercase)
multilang_alphabet_index = {letter: index for index, letter in enumerate(uk_ru_en_uppercase)}

uk_upper = list(u"АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ")
ru_upper = list(u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
en_upper = list(string.ascii_uppercase)

uk_index = {letter: index for index, letter in enumerate(uk_upper)}
ru_index = {letter: index for index, letter in enumerate(ru_upper)}
en_index = {letter: index for index, letter in enumerate(en_upper)}
_EMPTY_DICT = {}


def alphabet_key(lang, letter):
    return globals().get(lang + '_index', _EMPTY_DICT).get(letter, ord(letter))


def multilang_alphabet_key(letter):
    return multilang_alphabet_index.get(letter, ord(letter))


class ForumPageSpeaker(Orderable):
    page = ParentalKey('core.ForumSpeakersPage', related_name='speakers')
    speaker_page = models.ForeignKey('core.SpeakerPage',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='+', verbose_name='speaker')

    def __unicode__(self):
        return "%s -> %s (%s)" % (self.page.title, self.speaker_page.title, self.speaker_page.url)


class ForumSpeakersPage(TranslatablePage, BrowsableMixin):
    def get_context(self, request, *args, **kwargs):
        context = super(ForumSpeakersPage, self).get_context(request)

        letter = request.GET.get('letter')  # todo get from request
        if not letter:
            speakers = self.speakers.all()
        else:
            speakers = [link for link in self.speakers.all()
                        if guess_speaker_lastname(link.speaker_page)[0].upper() == letter]

        context['speakers'] = speakers
        return context

    @property
    def all_lang_letters(self):
        lang = translation.get_language()
        return globals().get(lang + '_upper', [])

    _speakers_letters = None

    @property
    def speakers_letters(self):
        if not self._speakers_letters:
            self._speakers_letters = set(guess_speaker_lastname(speaker.speaker_page)[0].upper()
                                         for speaker in self.speakers.all())
        return self._speakers_letters

    parent_page_types = ['core.ForumPage']


ForumSpeakersPage.content_panels = [
    FieldPanel('title', classname='title full'),
    InlinePanel(ForumSpeakersPage, 'speakers', label="Speakers")
]
ForumSpeakersPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(ForumSpeakersPage, fields=('title', ), languages=MODELS_LANGUAGES)


class ForumLocationPage(TranslatablePage, BrowsableMixin):
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='+')

    name = models.CharField(max_length=255, null=True, blank=True)
    name_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")
    name_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")

    city = models.CharField(max_length=255, null=True, blank=True)
    city_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    city_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")

    street = models.CharField(max_length=255, null=True, blank=True)
    street_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    street_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")

    country = models.CharField(max_length=255, null=True, blank=True)
    country_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")
    country_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")

    zip_code = models.CharField(max_length=20, null=True, blank=True, verbose_name="zip_code")
    link = models.URLField(null=True, blank=True)
    map_code = models.CharField(max_length=255, blank=True, default='', verbose_name="map_code")

    parent_page_types = ['core.ForumPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('name', classname="full"),
        FieldPanel('country', classname="full"),
        FieldPanel('city', classname="full"),
        FieldPanel('street', classname="full"),
        FieldPanel('zip_code', classname="full"),
        FieldPanel('link', classname="full"),
        FieldPanel('map_code', classname="full"),
    ]
    ru_panels = [
        FieldPanel('title_ru', classname="full title"),
        FieldPanel('name_ru', classname="full"),
        FieldPanel('country_ru', classname="full"),
        FieldPanel('city_ru', classname="full"),
        FieldPanel('street_ru', classname="full"),
    ]
    en_panels = [
        FieldPanel('title_en', classname="full title"),
        FieldPanel('name_en', classname="full"),
        FieldPanel('country_en', classname="full"),
        FieldPanel('city_en', classname="full"),
        FieldPanel('street_en', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(ForumLocationPage, fields=('title', 'name', 'country', 'city', 'street'),
                                languages=MODELS_LANGUAGES)


class ForumRegistrationPage(TranslatablePage, BrowsableMixin):
    parent_page_types = ['core.ForumPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(ForumRegistrationPage, fields=('title', ), languages=MODELS_LANGUAGES)

from django import forms


class SingleLineTextField(Field):
    description = _("Text")

    def get_internal_type(self):
        return "TextField"

    def get_prep_value(self, value):
        value = super(SingleLineTextField, self).get_prep_value(value)
        if isinstance(value, six.string_types) or value is None:
            return value
        return smart_text(value)

    def formfield(self, **kwargs):
        # Passing max_length to forms.CharField means that the value's length
        # will be validated twice. This is considered acceptable since we want
        # the value in the form field (to pass into widget for example).
        defaults = {'max_length': self.max_length, 'widget': forms.TextInput}
        defaults.update(kwargs)
        return super(SingleLineTextField, self).formfield(**defaults)


class ForumPackagesPageDateRanges(models.Model):
    page = ParentalKey('core.ForumPackagesPage', related_name='date_ranges')

    title = models.CharField(max_length=100, blank=True, default='')
    title_ru = models.CharField(max_length=100, blank=True, default='')
    title_en = models.CharField(max_length=100, blank=True, default='')


class ForumPackagesPageItem(models.Model):
    page = ParentalKey('core.ForumPackagesPage', related_name='packages')

    title = models.CharField(max_length=100, blank=True, default='')
    title_ru = models.CharField(max_length=100, blank=True, default='', verbose_name='title')
    title_en = models.CharField(max_length=100, blank=True, default='', verbose_name='title')

    description = SingleLineTextField(null=True, blank=True, default='')
    description_ru = SingleLineTextField(null=True, blank=True, default='', verbose_name='Description')
    description_en = SingleLineTextField(null=True, blank=True, default='', verbose_name='Description')

    prices = models.CommaSeparatedIntegerField(max_length=100, null=True, blank=True)

    panels = [

        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('description'),
            FieldPanel('prices'),
        ], heading='Default', classname='uk'),

        MultiFieldPanel([
            FieldPanel('title_ru'),
            FieldPanel('description_ru'),
        ], heading='RU', classname='ru'),

        MultiFieldPanel([
            FieldPanel('title_en'),
            FieldPanel('description_en'),
        ], heading='EN', classname='en'),

    ]

    @property
    def price_list(self):
        return self.prices.split(',')


class ForumPackagesPage(TranslatablePage, BrowsableMixin):
    parent_page_types = ['core.ForumPage']


ForumPackagesPage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel(ForumPackagesPage, 'date_ranges', label='Date Ranges'),
    InlinePanel(ForumPackagesPage, 'packages', label='Packages'),
]
ForumPackagesPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(ForumPackagesPage, fields=('title', ), languages=MODELS_LANGUAGES)


class ForumPage(TranslatablePage, BrowsableMixin):

    title_long = models.CharField(max_length=100, blank=True, default='')
    title_long_ru = models.CharField(max_length=100, blank=True, default='', verbose_name='title_long')
    title_long_en = models.CharField(max_length=100, blank=True, default='', verbose_name='title_long')

    date_from = models.DateField("Start date")
    date_to = models.DateField("End date", null=True, blank=True, help_text="Not required if event is on a single day")

    description = RichTextField(null=True, blank=True)
    description_ru = RichTextField(null=True, blank=True, verbose_name='description')
    description_en = RichTextField(null=True, blank=True, verbose_name='description')

    signup_link = models.URLField(blank=True)

    report_text = RichTextField(null=True, blank=True)
    report_text_ru = RichTextField(null=True, blank=True, verbose_name='report text')
    report_text_en = RichTextField(null=True, blank=True, verbose_name='report text')

    def _create_sub_pages(self):
        pass

    def save(self, *args, **kwargs):
        is_new = self.id is None
        super(ForumPage, self).save(*args, **kwargs)

        if is_new:
            self._create_sub_pages()

    @property
    def forum_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(ForumIndexPage).last()

    @property
    def speakers_page(self):
        return self.get_descendants().type(ForumSpeakersPage).live().last()

    @property
    def program(self):
        return self.get_descendants().type(ProgramPage).live().first().specific.sections

    @property
    def videos_list(self):
        lang = translation.get_language()
        videos = [page for page in self.videos.all() if page.video.language == lang]
        return videos

    @property
    def documents_list(self):
        lang = translation.get_language()
        documents = [page for page in self.documents.all() if page.doc.language == lang]
        return documents

    @property
    def albums_list(self):
        lang = translation.get_language()
        albums = [page for page in self.albums.all() if page.album.language == lang]
        return albums

    search_fields = Page.search_fields + (
        index.SearchField('title_ru', partial_match=True, boost=2),
        index.SearchField('title_en', partial_match=True, boost=2),
        index.SearchField('title_long', partial_match=True, boost=2),
        index.SearchField('title_long', partial_match=True, boost=2),
        index.SearchField('title_long_ru', partial_match=True, boost=2),
        index.SearchField('title_long_en', partial_match=True, boost=2),
        index.SearchField('description', partial_match=True),
        index.SearchField('description_ru', partial_match=True),
        index.SearchField('description_en', partial_match=True),
        index.SearchField('report_text', partial_match=True),
        index.SearchField('report_text_ru', partial_match=True),
        index.SearchField('report_text_en', partial_match=True),
    )


ForumPage.content_panels = [

    FieldPanel('title', classname="full title"),
    FieldPanel('title_long', classname="full title"),
    FieldPanel('description', classname="full"),
    FieldPanel('signup_link', classname="full"),

    MultiFieldPanel([
        FieldRowPanel([
            FieldPanel('date_from', classname='col6'),
            FieldPanel('date_to', classname='col6'),
        ]),
    ], heading="Dates"),

    FieldPanel('report_text', classname="full"),
]

ForumPage.ru_panels = [
    FieldPanel('title_ru', classname="full title"),
    FieldPanel('title_long_ru', classname="full title"),
    FieldPanel('description_ru', classname="full"),

    FieldPanel('report_text_ru', classname="full"),
]

ForumPage.en_panels = [
    FieldPanel('title_en', classname="full title"),
    FieldPanel('title_long_en', classname="full title"),
    FieldPanel('description_en', classname="full"),

    FieldPanel('report_text_en', classname="full"),
]

ForumPage.materials_panels = [
    InlinePanel(ForumPage, 'videos', label='Videos'),
    InlinePanel(ForumPage, 'albums', label='Albums'),
    InlinePanel(ForumPage, 'documents', label='Documents'),
]

ForumPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

PAGE_EDIT_HANDLERS[ForumPage] = TranslatableTabbedInterface([
    ObjectList(ForumPage.content_panels, heading='Content'),
    ObjectList(ForumPage.ru_panels, heading='RU'),
    ObjectList(ForumPage.en_panels, heading='EN'),
    ObjectList(ForumPage.materials_panels, heading='Materials'),
    ObjectList(ForumPage.promote_panels, heading='Promote'),
    ObjectList(ForumPage.settings_panels, heading='Settings', classname="settings")
])


class ContentPage(TranslatablePage, BrowsableMixin):
    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True, verbose_name='body')
    body_en = RichTextField(blank=True, null=True, verbose_name='body')

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    search_fields = [
        index.SearchField('title'),
        index.SearchField('title_ru'),
        index.SearchField('title_en'),
        index.SearchField('body', partial_match=True),
        index.SearchField('body_ru', partial_match=True),
        index.SearchField('body_en', partial_match=True),
    ]


register_translatable_interface(ContentPage, fields=('title', 'body'), languages=MODELS_LANGUAGES)


class ContactsPage(TranslatablePage, BrowsableMixin):
    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True)
    body_en = RichTextField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(ContactsPage, fields=('title', 'body'), languages=MODELS_LANGUAGES)


class PressTopPage(BaseMaterialPage):
    date = models.DateField(default=datetime.now)

    description = models.TextField(blank=True, null=True)

    content = RichTextField(blank=True, null=True, default='')

    subpage_types = []
    parent_page_types = ['core.NewsIndexPage', 'core.PressTopListPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('language'),
        FieldPanel('date', classname="date"),
        FieldPanel('description', classname="full"),
        FieldPanel('content', classname="full"),
    ]


class PressTopListPage(TranslatablePage, BrowsableMixin):

    def items(self):
        items = PressTopPage.objects.live().filter(**current_lang_filter_params())
        return items

    def get_context(self, request, **kwargs):
        press_releases = self.items()
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(press_releases, DEFAULT_PAGE_SIZE)
        try:
            press_releases = paginator.page(page)
        except PageNotAnInteger:
            press_releases = paginator.page(1)
        except EmptyPage:
            press_releases = paginator.page(paginator.num_pages)
        # Update template context
        context = super(PressTopListPage, self).get_context(request)
        context['press_releases'] = press_releases
        return context

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    subpage_types = ['core.PressTopPage']


register_translatable_interface(PressTopListPage, fields=('title', ), languages=MODELS_LANGUAGES)






class BaseHomePageAdvertPlacement(Orderable, models.Model):
    advert = models.ForeignKey('core.Advert', related_name='+')

    class Meta:
        abstract = True
        verbose_name = "Advert Placement"
        verbose_name_plural = "Advert Placements"

    def __unicode__(self):
        return self.page.title
        # return self.page.title + " -> " + self.advert.url

    panels = [
        SnippetChooserPanel('advert', Advert),
    ]


class HomePageAdvertPlacement(BaseHomePageAdvertPlacement):
    page = ParentalKey('core.HomePage', related_name='advert_placements')


class HomePageAdvertPlacementRU(BaseHomePageAdvertPlacement):
    page = ParentalKey('core.HomePage', related_name='advert_placements_ru')


class HomePageAdvertPlacementEN(BaseHomePageAdvertPlacement):
    page = ParentalKey('core.HomePage', related_name='advert_placements_en')


class HomePageMaterialVideo(Orderable):
    page = ParentalKey('core.HomePage', related_name='material_videos')
    video = models.ForeignKey('core.VideoPage', related_name='+')

    panels = [PageParentedChooserPanel('video', page_type=VideoPage, parent_cls=MaterialsVideoPage)]


class HomePageNews(Orderable, models.Model):
    page = ParentalKey('core.HomePage', related_name='news')

    news = models.ForeignKey(NewsPage,
                             null=True, blank=True,
                             on_delete=models.SET_NULL,
                             related_name='+')

    # panels = [ PageChooserPanel('news', page_type=NewsPage) ]
    panels = [ PageParentedChooserPanel('news', page_type=NewsPage, parent_cls=NewsIndexPage) ]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.news.title)


class HomePage(TranslatablePage, BrowsableMixin):
    forum_page = models.ForeignKey('core.ForumPage', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='+')

    # @property
    # def top_news(self):
    #     news = NewsPage.objects.live().filter(**current_lang_filter_params()).order_by('-date')
    #     return news

    @property
    def top_news(self):
        news = self.news.all()
        lang = translation.get_language()
        news = [page.news for page in news if page.news.language == lang]
        return news

    @property
    def videos(self):
        videos = self.material_videos.all()
        lang = translation.get_language()
        videos = [video_page for video_page in videos if video_page.video.language == lang]
        return videos

    class Meta:
        verbose_name = "Homepage"


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    PageChooserPanel('forum_page', page_type=ForumPage),
    InlinePanel(HomePage, 'advert_placements', label="Adverts"),
]

HomePage.ru_panels = [
    FieldPanel('title_ru', classname='full title'),
    InlinePanel(HomePage, 'advert_placements_ru', label="Adverts"),
]

HomePage.en_panels = [
    FieldPanel('title_en', classname='full title'),
    InlinePanel(HomePage, 'advert_placements_en', label="Adverts"),
]

HomePage.videos_panels = [
    InlinePanel(HomePage, 'material_videos', label="Videos"),
]

HomePage.news_panels = [
    InlinePanel(HomePage, 'news', label='News'),
]

HomePage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

PAGE_EDIT_HANDLERS[HomePage] = TranslatableTabbedInterface([
    ObjectList(HomePage.content_panels, heading='Content'),
    ObjectList(HomePage.ru_panels, heading='RU'),
    ObjectList(HomePage.en_panels, heading='EN'),
    ObjectList(HomePage.videos_panels, heading='Videos'),
    ObjectList(HomePage.news_panels, heading='News'),
    ObjectList(HomePage.promote_panels, heading='Promote'),
    ObjectList(HomePage.settings_panels, heading='Settings', classname="settings")
])


PROGRAM_SECTION_TYPE_CHOISES = (
    ('PD', _('Plenary discussions')),
    ('PZ', _('Plenary session'))
)


class ProgramPage(TranslatablePage, BrowsableMixin):
    subpage_types = ['core.ProgramSectionPage']

    @property
    def sections(self):
        db_sections = self.get_descendants().type(ProgramSectionPage).live().all()
        sections =  map(lambda section:section.specific, db_sections)

        def section_sorter(section):
            return section.forum_day, section.start_time, section.end_time

        return sorted(sections, key=section_sorter)

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(ProgramPage, fields=('title',), languages=MODELS_LANGUAGES)


def get_forum_start_date():
    # print forum_child_page
    return ForumPage.objects.first().date_from


class ProgramSectionPage(TranslatablePage, BrowsableMixin):
    section_type = models.CharField(max_length=2, choices=PROGRAM_SECTION_TYPE_CHOISES, blank=True, null=True)
    forum_day = IntegerRangeField(min_value=1, max_value=10, default=1)
    start_time = models.TimeField(verbose_name='Start')
    end_time = models.TimeField(verbose_name='End')

    subpage_types = ['core.ForumPanelPage']
    parent_page_types = ['core.ProgramPage']

    def panels(self):
        return self.get_descendants().type(ForumPanelPage).all().live()

    # def __unicode__(self):
    #     return "{} ({} - {})".format(self.title, self.start_time, self.end_time)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('forum_day'),
        FieldPanel('section_type'),
        FieldRowPanel([
            FieldPanel('start_time', classname="col5"),
            FieldPanel('end_time', classname="col5"),
        ]),
    ]

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(ProgramSectionPage, fields=('title',), languages=MODELS_LANGUAGES)


class ForumPanelPageVideo(Orderable):
    page = ParentalKey('core.ForumPanelPage', related_name='videos')
    video = models.ForeignKey('core.VideoPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('video', page_type=VideoPage, parent_cls=MaterialsVideoPage)]


class ForumPanelPagePhotoAlbum(Orderable):
    page = ParentalKey('core.ForumPanelPage', related_name='albums')
    album = models.ForeignKey('core.PhotoAlbumPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('album', page_type=PhotoAlbumPage, parent_cls=MaterialsAlbumsPage)]


class ForumPanelPageDocument(Orderable):
    page = ParentalKey('core.ForumPanelPage', related_name='documents')
    doc = models.ForeignKey('core.DocumentPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageParentedChooserPanel('doc', page_type=DocumentPage, parent_cls=MaterialsDocumentsPage)]


class ForumPanelPage(TranslatablePage, BrowsableMixin):
    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True, verbose_name='body')
    body_en = RichTextField(blank=True, null=True, verbose_name='body')

    location = models.CharField(max_length=255, null=True, blank=True)
    location_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name='description')
    location_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='description')

    enable_link = models.BooleanField(default=False)

    parent_page_types = ['core.ProgramSectionPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('enable_link'),
        FieldPanel('body', classname="full"),
        FieldPanel('location', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(ForumPanelPage, fields=('title', 'body', 'location'),
                                languages=MODELS_LANGUAGES, materials=True)