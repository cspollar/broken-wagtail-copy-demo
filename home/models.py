from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        Page, on_delete=models.CASCADE, related_name="tagged_items"
    )


class HomePage(Page):
    pass


class BlogPage(Page):
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    promote_panels = Page.promote_panels + [
        FieldPanel("tags"),
    ]


class SubBlogPage(BlogPage):
    pass
