# coding=utf-8
from datetime import date
import re

from django.conf.urls import url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.shortcuts import render_to_response, redirect
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from django.utils.translation import ugettext_lazy as _, ugettext_lazy
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, PageChooserPanel, \
    FieldRowPanel, \
    ObjectList
from wagtail.wagtailadmin.views.pages import PAGE_EDIT_HANDLERS
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from core.edit_handlers import InlineTestPanel, TranslatableTabbedInterface, register_translatable_interface, \
    TranslatableInlinePanel


MODELS_LANGUAGES = ('ru', 'en')

BROWSABLE_PAGE_PROMOTE_PANELS = [
    MultiFieldPanel([
                        FieldPanel('slug'),
                        FieldPanel('seo_title'),
                        FieldPanel('show_in_menus'),
                        FieldPanel('is_browsable'),
                        FieldPanel('search_description'),
                    ], ugettext_lazy('Common page configuration'))
]


class BrowsableMixin(models.Model):
    is_browsable = models.BooleanField(default=True, help_text=_("Whether a browsable link to this page will "
                                                                 "appear in automatically generated menus"))

    class Meta:
        abstract = True


class AccreditationPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True)
    body_en = RichTextField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('body', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(AccreditationPage, fields=('title', 'body'), languages=MODELS_LANGUAGES)


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
                        ], heading='UK'),

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
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('link', classname="full link"),
        FieldPanel('description', classname="full description"),
    ]

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.link)


class PhotoAlbumPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    link = models.URLField(default='')

    date = models.DateField("date")

    def preview_url(self):
        match = re.search("sets/(?P<id>[0-9]+)", self.link)
        if match:
            id = match.group("id")
        else:
            return ''

        preview_url = 'http://flickrit.com/slideshowholder.php?height=100&size=big&setId=' + id + '&counter=true&thumbnails=2&transition=0&layoutType=responsive&sort=0&theme=1'
        return preview_url

    preview = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True, null=True, default='')
    description_ru = models.TextField(blank=True, null=True, default='', verbose_name='description')
    description_en = models.TextField(blank=True, null=True, default='', verbose_name='description')

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('date', classname="date"),
        FieldPanel('link', classname="link full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full"),
    ]


register_translatable_interface(PhotoAlbumPage, fields=('title', 'description'), languages=MODELS_LANGUAGES)


class DocumentPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    date = models.DateField("date")

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
    description_ru = models.TextField(blank=True, null=True, default='')
    description_en = models.TextField(blank=True, null=True, default='')

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('date', classname="date"),
        DocumentChooserPanel('doc'),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


register_translatable_interface(DocumentPage, fields=('title', 'description'), languages=MODELS_LANGUAGES)


class VideoPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    date = models.DateField("date")

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
    description_ru = models.TextField(blank=True, null=True, default='', verbose_name='description')
    description_en = models.TextField(blank=True, null=True, default='', verbose_name='description')

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('date', classname="date"),
        FieldPanel('link', classname="full"),
        FieldPanel('code', classname="full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


register_translatable_interface(VideoPage, fields=('title', 'description'), languages=MODELS_LANGUAGES)


class MaterialsPage(RoutablePageMixin, BrowsableMixin, Page):
    subpage_urls = (
        url(r'^$', 'main_view', name='main'),
        url(r'^videos/$', 'videos_view', name='videos'),
        url(r'^albums/$', 'albums_view', name='albums'),
        url(r'^documents/$', 'documents_view', name='documents'),
    )

    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    albums = lambda (self): PhotoAlbumPage.objects.live().all()
    documents = lambda (self): DocumentPage.objects.live().all()
    videos = lambda (self): VideoPage.objects.live().all()

    def main_view(self, request):
        return render_to_response("core/materials_page.html", {'self': self, 'request': request})

    def albums_view(self, request):
        return render_to_response("core/materials_albums_page.html", {'self': self, 'request': request})

    def documents_view(self, request):
        return render_to_response("core/materials_documents_page.html", {'self': self, 'request': request})

    def videos_view(self, request):
        return render_to_response("core/materials_video_page.html", {'self': self, 'request': request})

    def construct_menu(self):
        menu = [
            {'route_name': 'videos', 'title': _('videos')},
            {'route_name': 'albums', 'title': _('albums')},
            {'route_name': 'documents', 'title': _('documents')},
        ]
        return menu

    subpage_types = ['core.PhotoAlbumPage', 'core.DocumentPage', 'core.VideoPage']


register_translatable_interface(MaterialsPage, fields=('title', ), languages=MODELS_LANGUAGES)


class NewsPageVideo(Orderable):
    page = ParentalKey('core.NewsPage', related_name='videos')
    video = models.ForeignKey('core.VideoPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageChooserPanel('video', page_type=VideoPage)]


class NewsPagePhotoAlbum(Orderable):
    page = ParentalKey('core.NewsPage', related_name='albums')
    album = models.ForeignKey('core.PhotoAlbumPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageChooserPanel('album', page_type=PhotoAlbumPage)]


class NewsPageDocument(Orderable):
    page = ParentalKey('core.NewsPage', related_name='documents')
    doc = models.ForeignKey('core.DocumentPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [PageChooserPanel('doc', page_type=DocumentPage)]


class NewsPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    date = models.DateField("date")

    short = models.TextField()
    short_ru = models.TextField(blank=True, null=True, verbose_name='short')
    short_en = models.TextField(blank=True, null=True, verbose_name='short')

    body = RichTextField()
    body_ru = RichTextField(blank=True, null=True, verbose_name='body')
    body_en = RichTextField(blank=True, null=True, verbose_name='body')
    # tags = ClusterTaggableManager(through=NewsPageTag, blank=True)

    @property
    def news_index(self):
        # Find closest ancestor which is a index
        return self.get_ancestors().type(NewsIndexPage).last()

    search_fields = [

    ]


NewsPage.content_panels = [
    FieldPanel('title', classname="full title"),
    ImageChooserPanel('image'),
    FieldPanel("date"),
    FieldPanel("short"),
    FieldPanel("body", classname="full"),
    MultiFieldPanel([
                        InlinePanel(NewsPage, 'videos', label='Videos'),
                        InlinePanel(NewsPage, 'albums', label='Albums'),
                        InlinePanel(NewsPage, 'documents', label='Documents'),
                    ], heading="Materials", classname="collapsible collapsed")
]

register_translatable_interface(NewsPage, fields=('title', 'short', 'body'), languages=MODELS_LANGUAGES)


class NewsIndexPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    @property
    def news(self):
        # Get list of live blog  pages that are descendants of this page
        news = NewsPage.objects.live().descendant_of(self)
        # Order by most recent date first
        news = news.order_by('-date')
        return news

    def get_context(self, request, **kwargs):
        news = self.news
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            news = news.filter(tags__name=tag)
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(news, 10)  # Show 10 news per page
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

    subpage_types = ['core.NewsPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(NewsIndexPage, fields=('title',), languages=MODELS_LANGUAGES)


class OrgPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    @property
    def organizers(self):
        return OrganizerPage.objects.live().all()

    subpage_types = ['core.OrganizerPage']

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(OrgPage, fields=('title',), languages=MODELS_LANGUAGES)


class ParticipationPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))


register_translatable_interface(ParticipationPage, fields=('title',), languages=MODELS_LANGUAGES)


class RadaPageMember(Orderable):
    page = ParentalKey('core.RadaPage', related_name='members')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                             help_text=_("The page title as you'd like it to be seen by the public"))
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    position = models.CharField(max_length=255, blank=True, null=True, default='')
    position_ru = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')
    position_en = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='position')

    about = RichTextField(blank=True, null=True, default='')
    about_ru = RichTextField(blank=True, null=True, default='', verbose_name='about')
    about_en = RichTextField(blank=True, null=True, default='', verbose_name='about')

    panels = [
        MultiFieldPanel([
                            FieldPanel('title'),
                            ImageChooserPanel('photo'),
                            FieldPanel('position'),
                            FieldPanel('about'),
                        ], heading='UK', classname='uk'),
        MultiFieldPanel([
                            FieldPanel('title_ru'),
                            FieldPanel('position_ru'),
                            FieldPanel('about_ru'),
                        ], heading='RU', classname='ru'),
        MultiFieldPanel([
                            FieldPanel('title_en'),
                            FieldPanel('position_en'),
                            FieldPanel('about_en'),
                        ], heading='EN', classname='en'),
    ]


class RadaPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))


RadaPage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel(RadaPage, 'members', label='Members'),
]
RadaPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(RadaPage, fields=('title',), languages=MODELS_LANGUAGES)


class PartnerListPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    @property
    def partners(self):
        return Partner.objects.all()

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(PartnerListPage, fields=('title',), languages=MODELS_LANGUAGES)


class OrganizerPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

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


register_translatable_interface(OrganizerPage, fields=('title', 'description'), languages=MODELS_LANGUAGES)


class ForumIndexPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

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


register_translatable_interface(ForumIndexPage, fields=('title', ), languages=MODELS_LANGUAGES)


class ForumPageSpeaker(Orderable):
    forum_page = ParentalKey('core.ForumPage', related_name='speakers')
    speaker_page = models.ForeignKey('core.SpeakerPage',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='+')

    panels = [PageChooserPanel('speaker_page', page_type='core.SpeakerPage')]

    def __unicode__(self):
        return "%s -> %s (%s)" % (self.forum_page.title, self.speaker_page.title, self.speaker_page.url)


class ForumPageVideo(Orderable):
    page = ParentalKey('core.ForumPage', related_name='videos')
    video = models.ForeignKey(VideoPage,
                              null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+')

    panels = [PageChooserPanel('video', page_type=VideoPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.video.title)


class ForumPagePhotoAlbum(Orderable):
    page = ParentalKey('core.ForumPage', related_name='albums')
    album = models.ForeignKey(PhotoAlbumPage,
                              null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name='+')

    panels = [PageChooserPanel('album', page_type=PhotoAlbumPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.album.title)


class ForumPageDocument(Orderable):
    page = ParentalKey('core.ForumPage', related_name='documents')
    doc = models.ForeignKey(DocumentPage,
                            null=True, blank=True,
                            on_delete=models.SET_NULL,
                            related_name='+')

    panels = [PageChooserPanel('doc', page_type=DocumentPage)]

    def __unicode__(self):
        return "%s -> %s" % (self.page.title, self.doc.title)


class TimetableDayItem(models.Model):
    day = models.ForeignKey('core.TimetableDayItem', null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='timetable')
    # day = ParentalKey('core.ForumPageTimetableDay', related_name='timetable')
    title = models.CharField(max_length=255, blank=True, default='')
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, default='')
    description = RichTextField(blank=True)

    search_fields = (
        index.SearchField('title'),
        index.SearchField('title_ru'),
        index.SearchField('title_en'),
        index.SearchField('description'),
        index.SearchField('description'),
        index.SearchField('description'),
    )

    panels = [
        FieldPanel('title', classname="full"),
        FieldPanel('time_from', classname='col3'),
        FieldPanel('time_to', classname='col3'),
        FieldPanel('location'),
        FieldPanel('description'),
    ]


class ForumPageTimetableDay(Orderable):
    page = ParentalKey('core.ForumPage', related_name='timetable_days')
    title = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        print self
        return "%s Timetable" % self.page.title


ForumPageTimetableDay.panels = [
    FieldPanel('title'),
    # FieldPanel('timetable'),
    # InlinePanel(ForumPageTimetableDay, 'timetable', panels=TimetableDayItem.panels)
]


def guess_speaker_lastname(speaker):
    return speaker.title.split()[-1]


class ForumPage(RoutablePageMixin, BrowsableMixin, Page):
    subpage_urls = (
        url(r'^$', 'main_view', name='main'),
        url(r'^location/$', 'location_view', name='location'),
        url(r'^packages/$', 'packages_view', name='packages'),
        url(r'^timetable/$', 'timetable_view', name='timetable'),
        url(r'^speakers/$', 'speakers_view', name='speakers'),
        url(r'^speakers/(?P<letter>\w?)/$', 'speakers_view', name='speakers'),
        url(r'^registration/$', 'registration_view', name='registration'),
    )

    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    title_long = models.CharField(max_length=100, blank=True, default='')
    title_long_ru = models.CharField(max_length=100, blank=True, default='', verbose_name='title_long')
    title_long_en = models.CharField(max_length=100, blank=True, default='', verbose_name='title_long')

    date_from = models.DateField("Start date")
    date_to = models.DateField("End date", null=True, blank=True, help_text="Not required if event is on a single day")

    description = RichTextField(null=True, blank=True)
    description_ru = RichTextField(null=True, blank=True, verbose_name='description')
    description_en = RichTextField(null=True, blank=True, verbose_name='description')

    signup_link = models.URLField(blank=True)
    # location
    location_logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='+',
                                      verbose_name="logo")
    location_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")
    location_name_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")
    location_name_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")

    location_city = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    location_city_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    location_city_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")

    location_street = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    location_street_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    location_street_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")

    location_country = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")
    location_country_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")
    location_country_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")

    location_zip_code = models.CharField(max_length=20, null=True, blank=True, verbose_name="zip_code")
    location_map_code = models.CharField(max_length=255, blank=True, default='', verbose_name="map_code")
    # end location
    # report
    # has_report = models.BooleanField(default=False)
    report_text = RichTextField(null=True, blank=True)
    report_text_ru = RichTextField(null=True, blank=True, verbose_name='report_text')
    report_text_en = RichTextField(null=True, blank=True, verbose_name='report_text')
    # end report

    def is_navigable(self):
        return True

    @property
    def forum_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(ForumIndexPage).last()

    @property
    def speakers_letters(self):
        letters = sorted(set(guess_speaker_lastname(speaker.speaker_page)[0].upper()
                             for speaker in self.speakers.all()))
        return letters

    def main_view(self, request):
        return render_to_response('core/forum_page.html', {'self': self, 'request': request})

    def speakers_view(self, request, letter=None):
        if not letter:
            speakers = self.speakers.all()
        else:
            speakers = [speaker for speaker in self.speakers.all()
                        if guess_speaker_lastname(speaker.speaker_page)[0].upper() == letter]

        return render_to_response('core/forum_speakers_page.html', {
            'self': self,
            'request': request,
            'speakers': speakers
        })

    def location_view(self, request):
        return render_to_response('core/forum_location_page.html', {'self': self, 'request': request})

    def packages_view(self, request):
        return render_to_response('core/forum_packages_page.html', {'self': self, 'request': request})

    def timetable_view(self, request):
        return render_to_response('core/forum_timetable_page.html', {'self': self, 'request': request})

    def registration_view(self, request):
        return redirect(self.signup_link)

    def construct_menu(self):
        menu = [
            {'route_name': 'location', 'title': _('location')},
            {'route_name': 'packages', 'title': _('packages')},
            {'route_name': 'timetable', 'title': _('timetable')},
            {'route_name': 'speakers', 'title': _('speakers')},
            {'route_name': 'registration', 'title': _('registration')},
        ]
        return menu

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
    )


ForumPage.content_panels = [
    MultiFieldPanel([
                        FieldPanel('title', classname="full title"),
                        FieldPanel('title_long', classname="full title"),
                        FieldPanel('description', classname="full"),
                        FieldPanel('signup_link'),
                    ], heading="Main"),
    MultiFieldPanel([
                        FieldRowPanel([
                            FieldPanel('date_from', classname='col6'),
                            FieldPanel('date_to', classname='col6'),
                        ])
                    ], heading="Dates"),

    FieldPanel('report_text', classname="full"),

    MultiFieldPanel([
                        InlinePanel(ForumPage, 'videos', label='Videos'),
                        InlinePanel(ForumPage, 'albums', label='Albums'),
                        InlinePanel(ForumPage, 'documents', label='Documents'),
                    ], heading="Materials", classname="collapsible collapsed"),

    MultiFieldPanel([
                        FieldPanel('location_name'),
                        ImageChooserPanel('location_logo'),
                        FieldPanel('location_country'),
                        FieldPanel('location_city'),
                        FieldPanel('location_street'),
                        FieldPanel('location_zip_code'),
                        FieldPanel('location_map_code'),
                    ], heading="Location", classname="collapsible collapsed"),

    # MultiFieldPanel([
    # InlinePanel(ForumPage, 'timetable_days', label="Day"),
    InlinePanel(ForumPage, 'timetable_days', label="Day"),
    # ], heading="Timetable", classname="collapsible collapsed"),

    MultiFieldPanel([
                        InlinePanel(ForumPage, 'speakers', label="Speakers"),
                    ], heading="Speakers", classname="collapsible collapsed")
]

ForumPage.ru_panels = [
    MultiFieldPanel([
                        FieldPanel('title_ru', classname="full title"),
                        FieldPanel('title_long_ru', classname="full title"),
                        FieldPanel('description_ru', classname="full"),
                    ], heading="Main"),

    FieldPanel('report_text_ru', classname="full"),

    MultiFieldPanel([
                        FieldPanel('location_name_ru'),
                        FieldPanel('location_country_ru'),
                        FieldPanel('location_city_ru'),
                        FieldPanel('location_street_ru'),
                    ], heading="Location", classname="collapsible collapsed"),
]

ForumPage.en_panels = [
    MultiFieldPanel([
                        FieldPanel('title_en', classname="full title"),
                        FieldPanel('title_long_en', classname="full title"),
                        FieldPanel('description_en', classname="full"),
                    ], heading="Main"),

    FieldPanel('report_text_en', classname="full"),

    MultiFieldPanel([
                        FieldPanel('location_name_en'),
                        FieldPanel('location_country_en'),
                        FieldPanel('location_city_en'),
                        FieldPanel('location_street_en'),
                    ], heading="Location", classname="collapsible collapsed"),
]

ForumPage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

PAGE_EDIT_HANDLERS[ForumPage] = TranslatableTabbedInterface([
    ObjectList(ForumPage.content_panels, heading='Content'),
    ObjectList(ForumPage.ru_panels, heading='RU'),
    ObjectList(ForumPage.en_panels, heading='EN'),
    ObjectList(ForumPage.promote_panels, heading='Promote'),
    ObjectList(ForumPage.settings_panels, heading='Settings', classname="settings")
])

# register_translatable_interface(ForumPage,
# fields=('title', 'title_long', 'description',
#                                         'location_name', 'location_city', 'location_street', 'location_country',
#                                         'report_text'),
#                                 languages=MODELS_LANGUAGES)


class ForumTimetablePage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    comment = RichTextField(blank=True, null=True)
    comment_ru = RichTextField(blank=True, null=True, verbose_name='comment')
    comment_en = RichTextField(blank=True, null=True, verbose_name='comment')

    content_panels = [
        FieldPanel('title', classname='title full'),
        FieldPanel('comment', classname='full'),
    ]


register_translatable_interface(ForumTimetablePage, fields=('title', 'comment'), languages=MODELS_LANGUAGES)


class ForumTimetableItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    title_ru = models.CharField(max_length=255, blank=True, null=True, default='')
    title_en = models.CharField(max_length=255, blank=True, null=True, default='')

    time_from = models.DateTimeField("Start time", null=True, blank=True)
    time_to = models.DateTimeField("End time", null=True, blank=True)

    location = models.CharField(max_length=255, blank=True, default='')
    location_ru = models.CharField(max_length=255, blank=True, default='', verbose_name='location')
    location_en = models.CharField(max_length=255, blank=True, default='', verbose_name='location')

    description = RichTextField(blank=True, null=True)
    description_ru = RichTextField(blank=True, null=True, verbose_name='description')
    description_en = RichTextField(blank=True, null=True, verbose_name='description')


class SpeakerPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

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


register_translatable_interface(SpeakerPage, fields=('title', 'position', 'about'), languages=MODELS_LANGUAGES)


class AllSpeakersIndexPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    def speakers(self):
        speakers = SpeakerPage.objects.live().descendant_of(self)
        return speakers

    subpage_types = ['core.SpeakerPage']

    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(AllSpeakersIndexPage, fields=('title', ), languages=MODELS_LANGUAGES)


class ContentPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

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


class ContactsPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    body = RichTextField(blank=True, null=True)
    body_ru = RichTextField(blank=True, null=True)
    body_en = RichTextField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS


register_translatable_interface(ContactsPage, fields=('title', 'body'), languages=MODELS_LANGUAGES)


class PressTopPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    date = models.DateField()

    description = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True, verbose_name='description')
    description_en = models.TextField(blank=True, null=True, verbose_name='description')

    content = RichTextField(blank=True, null=True, default='')
    content_ru = RichTextField(blank=True, null=True, default='', verbose_name='content')
    content_en = RichTextField(blank=True, null=True, default='', verbose_name='content')

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date', classname="date"),
        FieldPanel('description', classname="full"),
        FieldPanel('content', classname="full"),
    ]


register_translatable_interface(PressTopPage, fields=('title', 'description', 'content'), languages=MODELS_LANGUAGES)


class PressTopListPage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    def items(self):
        items = PressTopPage.objects.live().all()
        return items

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]
    promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

    subpage_types = ['core.PressTopPage']


register_translatable_interface(PressTopListPage, fields=('title', ), languages=MODELS_LANGUAGES)


class HomePageAdvertPlacement(Orderable, models.Model):
    page = ParentalKey('core.HomePage', related_name='advert_placements')
    advert = models.ForeignKey('core.Advert', related_name='+')

    class Meta:
        verbose_name = "Advert Placement"
        verbose_name_plural = "Advert Placements"

    def __unicode__(self):
        return self.page.title
        # return self.page.title + " -> " + self.advert.url

    panels = [
        SnippetChooserPanel('advert', Advert),
    ]


class HomePageMaterialVideo(Orderable):
    page = ParentalKey('core.HomePage', related_name='material_videos')
    video = models.ForeignKey('core.VideoPage', related_name='+')

    panels = [
        PageChooserPanel('video', page_type=VideoPage),
    ]


class HomePage(Page, BrowsableMixin):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='title',
                                help_text=_("The page title as you'd like it to be seen by the public"))

    forum_page = models.ForeignKey('core.ForumPage', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='+')

    @property
    def top_news(self):
        news = NewsPage.objects.live().descendant_of(self).order_by('-date')  # or get News Page
        return news

    class Meta:
        verbose_name = "Homepage"


HomePage.content_panels = Page.content_panels + [
    PageChooserPanel('forum_page', page_type=ForumPage),
    InlinePanel(HomePage, 'material_videos', label="Videos"),
    InlinePanel(HomePage, 'advert_placements', label="Adverts"),
]

HomePage.promote_panels = BROWSABLE_PAGE_PROMOTE_PANELS

register_translatable_interface(HomePage, fields=('title',), languages=MODELS_LANGUAGES)
