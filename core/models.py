# coding=utf-8
from datetime import date

from django.conf.urls import url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.shortcuts import render_to_response, redirect
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class AccreditationPage(Page):
    body = RichTextField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('body', classname="full"),
    ]


class ArchivePage(Page):
    pass


class BussinesPage(Page):
    pass


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
    button_text = models.CharField(max_length=50, null=True, blank=True)
    button_link = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('text', classname="full"),
        MultiFieldPanel([
            FieldPanel('button_text'),
            FieldPanel('button_link'),
        ])
    ]

    def __unicode__(self):
        return strip_tags(self.text.replace(">", "> "))


@register_snippet
class Partner(models.Model):
    title = models.CharField(max_length=255, help_text=_("The title as you'd like it to be seen by the public"))
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('link', classname="full link"),
        FieldPanel('description', classname="full description"),
    ]

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.link)


class PhotoAlbumPage(Page):
    link = models.URLField(default='')

    preview = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True, null=True, default='')

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('link', classname="link full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full"),
    ]


class DocumentPage(Page):
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

    content_panels = [
        # FieldPanel('title', classname="title full"),
        # DocumentChooserPanel('doc'),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


class VideoPage(Page):
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

    content_panels = [
        FieldPanel('title', classname="title full"),
        FieldPanel('link', classname="full"),
        FieldPanel('code', classname="full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


class MaterialsPage(RoutablePageMixin, Page):
    subpage_urls = (
        url(r'^$', 'materials', name='materials'),
        url(r'^videos/$', 'videos_view', name='videos_view'),
        url(r'^albums/$', 'albums_view', name='albums_view'),
        url(r'^documents/$', 'documents_view', name='documents_view'),
    )

    def albums(self):
        albums = PhotoAlbumPage.objects.live().all()
        return albums

    def documents(self):
        documents = DocumentPage.objects.live().all()
        return documents

    def videos(self):
        videos = VideoPage.objects.live().all()
        return videos


    def materials(self, request):
        return render_to_response("core/materials_page.html", {'self': self, 'request': request})

    def albums_view(self, request):
        return render_to_response("core/materials_albums_page.html", {'self': self, 'request': request})

    def documents_view(self, request):
        return render_to_response("core/materials_documents_page.html", {'self': self, 'request': request})

    def videos_view(self, request):
        return render_to_response("core/materials_video_page.html", {'self': self, 'request': request})

    subpage_types = ['core.PhotoAlbumPage', 'core.DocumentPage', 'core.VideoPage']


# class NewsPageTag(TaggedItemBase):
# content_object = ParentalKey('core.NewsPage', related_name='tagged_items')


class NewsPage(Page):
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    date = models.DateField("date")
    short = models.TextField()
    body = RichTextField()
    # tags = ClusterTaggableManager(through=NewsPageTag, blank=True)

    @property
    def news_index(self):
        # Find closest ancestor which is a index
        return self.get_ancestors().type(NewsIndexPage).last()

    subpage_types = ['core.NewsPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('image'),
        FieldPanel("date"),
        FieldPanel("short"),
        FieldPanel("body", classname="full"),
    ]


class NewsIndexPage(Page):
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


class OrgPage(Page):
    @property
    def organizers(self):
        return OrganizerPage.objects.live().all()

    subpage_types = ['core.OrganizerPage']


class PanelPage(Page):
    pass


class ParticipationPage(Page):
    pass


class RadaPage(Page):
    pass


class PartnerListPage(Page):
    @property
    def partners(self):
        return Partner.objects.all()


# class PartnerPage(Page):
# logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# description = models.TextField()
# link = models.URLField()
#
# content_panels = [
# FieldPanel('title', classname="full title"),
#         ImageChooserPanel('logo'),
#         FieldPanel('link', classname="full link"),
#         FieldPanel('description', classname="full description"),
#     ]


class OrganizerPage(Page):
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('link', classname="full link"),
        FieldPanel('description', classname="full description"),
    ]


class ForumIndexPage(Page):
    @property
    def forums(self):
        # Get list of live event pages that are descendants of this page
        forums = ForumPage.objects.live().descendant_of(self)
        # Filter events list to get ones that are either
        # running now or start in the future
        forums = forums.filter(date_from__gte=date.today())
        # Order by date
        forums = forums.order_by('date_from')
        return forums

    subpage_types = ['core.ForumPage']

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]


class ForumPageSpeaker(Orderable):
    forum_page = ParentalKey('core.ForumPage', related_name='speakers')
    speaker_page = models.ForeignKey('core.SpeakerPage',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='+')

    panels = [
        PageChooserPanel('speaker_page', page_type='core.SpeakerPage')
    ]

    def __unicode__(self):
        return "%s -> %s (%s)" % (self.forum_page.title, self.speaker_page.title, self.speaker_page.url)


class ForumPage(RoutablePageMixin, Page):
    subpage_urls = (
        url(r'^$', 'forum', name='forum'),
        url(r'^location/$', 'location', name='location'),
        url(r'^packages/$', 'packages', name='packages'),
        url(r'^timetable/$', 'timetable', name='timetable'),
        url(r'^speakers/$', 'speakers_view', name='speakers_view'),
        url(r'^registration/$', 'registration', name='registration'),
    )

    title_long = models.CharField(max_length=100, blank=True, default='')
    date_from = models.DateField("Start date")
    date_to = models.DateField("End date", null=True, blank=True, help_text="Not required if event is on a single day")
    description = RichTextField(null=True)
    signup_link = models.URLField(blank=True)
    has_report = models.BooleanField(default=False)
    # location
    location_logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='+',
                                      verbose_name="logo")
    location_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="name")
    location_city = models.CharField(max_length=255, null=True, blank=True, verbose_name="city")
    location_street = models.CharField(max_length=255, null=True, blank=True, verbose_name="street")
    location_country = models.CharField(max_length=255, null=True, blank=True, verbose_name="country")
    location_zip_code = models.CharField(max_length=20, null=True, blank=True, verbose_name="zip_code")
    location_map_code = models.CharField(max_length=255, blank=True, default='', verbose_name="map_code")
    # end location


    @property
    def forum_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(ForumIndexPage).last()

    def forum(self, request):
        return render_to_response('core/forum_page.html', {'self': self, 'request': request})

    def speakers_view(self, request):
        return render_to_response('core/forum_speakers_page.html', {'self': self, 'request': request})

    def location(self, request):
        return render_to_response('core/forum_location_page.html', {'self': self, 'request': request})

    def packages(self, request):
        return render_to_response('core/forum_packages_page.html', {'self': self, 'request': request})

    def timetable(self, request):
        return render_to_response('core/forum_timetable_page.html', {'self': self, 'request': request})

    def registration(self, request):
        return redirect(self.signup_link)


    search_fields = Page.search_fields + (
        index.SearchField('title_long'),
        index.SearchField('description'),
    )


ForumPage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title', classname="full title"),
        FieldPanel('title_long', classname="full title"),
        FieldPanel('description', classname="full"),
        FieldPanel('signup_link'),
    ], heading="Main"),
    MultiFieldPanel([
        FieldPanel('date_from'),
        FieldPanel('date_to'),
    ], heading="Dates"),
    FieldPanel('has_report'),

    MultiFieldPanel([
        FieldPanel('location_name'),
        ImageChooserPanel('location_logo'),
        FieldPanel('location_country'),
        FieldPanel('location_city'),
        FieldPanel('location_street'),
        FieldPanel('location_zip_code'),
        FieldPanel('location_map_code'),
    ], heading="Location", classname="collapsible collapsed"),

    MultiFieldPanel([
        InlinePanel(ForumPage, 'speakers', label="Speakers"),
    ], heading="Speakers", classname="collapsible collapsed")
]


class ForumTimetablePage(Page):
    comment = RichTextField(blank=True)


class ForumTimetableItem(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    time_from = models.DateTimeField("Start time", null=True, blank=True)
    time_to = models.DateTimeField("End time", null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, default='')
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )


class SpeakerPage(Page):
    # full_name = models.CharField(max_length=100, blank=True, default='')
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    position = models.CharField(max_length=255, blank=True, default='')
    about = RichTextField(blank=True, default='')

    # def url(self):
    #     return self.url_path

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('photo'),
        FieldPanel('position'),
        FieldPanel('about', classname="full"),
    ]


class AllSpeakersIndexPage(Page):

    def speakers(self):
        speakers = SpeakerPage.objects.live().descendant_of(self)
        return speakers

    subpage_types = ['core.SpeakerPage']


class ContentPage(Page):
    body = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
    ]


class ContactsPageItem(Orderable):
    page = ParentalKey('core.ContactsPage', related_name='items')
    title = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField()

    def __unicode__(self):
        return self.title


class ContactsPage(Page):
    pass


ContactsPage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel(ContactsPage, 'items', label="Contacts"),
]


class PressTopPage(Page):
    date = models.DateField()
    description = models.TextField()
    content = RichTextField(default='')

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date', classname="date"),
        FieldPanel('description', classname="full description"),
        FieldPanel('content', classname="full content"),
    ]


class PressTopListPage(Page):

    def items(self):
        items = PressTopPage.objects.all()
        return items

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]

    subpage_types = ['core.PressTopPage']


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


class HomePage(Page):
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
