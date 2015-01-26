from django.db import models
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page

class AccreditationPage(Page):
    pass

class ArchivePage(Page):
    pass

class BussinesPage(Page):
    pass

class HomePage(Page):
    pass

class MaterialsPage(Page):
    pass

class NewsPage(Page):
    pass

class OrgPage(Page):
    pass

class PanelPage(Page):
    pass

class ParticipationPage(Page):
    pass

class ProgramPage(Page):
    pass

class RadaPage(Page):
    pass

class SpeakerPage(Page):
    pass

class SpeakersPage(Page):
    pass

class ContentPage(Page):
    content = RichTextField()
    pass

class EmptyPage(Page):
    pass