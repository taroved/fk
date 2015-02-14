from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from django.utils.translation import ugettext_lazy as _
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class AccreditationPage(Page):
    pass


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


class HomePageVideoItem(Orderable):
    page = ParentalKey('core.HomePage', related_name='videos')
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

    panels = [
        FieldPanel('link', classname="full"),
        FieldPanel('code', classname="full"),
        ImageChooserPanel('preview'),
        FieldPanel('description', classname="full")
    ]


class MaterialsPage(Page):
    subpage_types = ['core.PhotoAlbumPage', 'core.DocumentPage', 'core.VideoPage']


class NewsPageTag(TaggedItemBase):
    content_object = ParentalKey('core.NewsPage', related_name='tagged_items')


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
    subpage_types = ['core.OrganizatorPage']


class PanelPage(Page):
    pass


class ParticipationPage(Page):
    pass


class RadaPage(Page):
    pass


class PartnerListPage(Page):
    subpage_types = ['core.PartnerPage']


class PartnerPage(Page):
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    description = models.TextField()
    link = models.URLField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('logo'),
        FieldPanel('description', classname="full description"),
        FieldPanel('link', classname="full link"),
    ]


class OrganizatorPage(PartnerPage):
    pass


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


class ForumPage(Page):
    title_long = models.CharField(max_length=100, blank=True, default='')
    date_from = models.DateField("Start date")
    date_to = models.DateField("End date", null=True, blank=True, help_text="Not required if event is on a single day")
    description = RichTextField(null=True)
    signup_link = models.URLField(blank=True)

    has_report = models.BooleanField(default=False)

    @property
    def forum_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(ForumIndexPage).last()

    subpage_types = ['core.ForumLocationPage', 'core.ForumTimetablePage', 'core.ContentPage']

    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )


ForumPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('title_long', classname="full title"),
    FieldPanel('type'),
    FieldPanel('date_from'),
    FieldPanel('date_to'),
    FieldPanel('signup_link'),
    FieldPanel('description', classname="full"),
    FieldPanel('has_report'),
    InlinePanel(ForumPage, 'speakers', label="Speakers"),
]


class ForumLocationPage(Page):
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, default='')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


ForumLocationPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('name'),
    ImageChooserPanel('logo'),
    FieldPanel('country'),
    FieldPanel('city'),
    FieldPanel('street'),
    FieldPanel('zip_code'),
    FieldPanel('location'),
    FieldPanel('latitude'),
    FieldPanel('longitude'),
]


class ForumTimetablePage(Page):
    comment = RichTextField(blank=True)


class ForumTimetableItem(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, default='')
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )


class SpeakerPage(Page):
    # full_name = models.CharField(max_length=100, blank=True, default='')
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    position = models.CharField(max_length=100, blank=True, default='')
    about = RichTextField(blank=True, default='')

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
        return self.page.title + " -> " + self.advert.url

    panels = [
        SnippetChooserPanel('advert', Advert),
    ]


class HomePage(Page):
    forum_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='+')

    @property
    def top_news(self):
        news = NewsPage.objects.live().descendant_of(self).order_by('-date')  # or get News Page
        return news

    class Meta:
        verbose_name = "Homepage"


HomePage.content_panels = Page.content_panels + [
    PageChooserPanel('forum_page', page_type=ForumPage),
    InlinePanel(HomePage, 'videos', label="Videos", panels=HomePageVideoItem.panels),
    InlinePanel(HomePage, 'advert_placements', label="Adverts"),
]
