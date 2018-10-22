from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import CalloutBlock


class HomePage(Page):

    body = StreamField([
        ('callout', CalloutBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]