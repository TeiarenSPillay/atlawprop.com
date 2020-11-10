from eos.news.models import Article
from django.template import resolve_variable
from django.template import Variable
from django import template
import random


register = template.Library()


class GetArticleByCategory(template.Node):

    def __init__(self, category_slug):
        self.category_slug = category_slug

    def render(self, context):
        category_slug = resolve_variable(self.category_slug, context)

        articles = Article.objects.filter(
            status="Active",
            category__slug=category_slug
        ).order_by('-date_added')

        context['articles'] = articles

        return ''


@register.tag(name="get_article_by_category")
def get_article_by_category(parser, token):
    try:
        tag_name, category_slug = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "get_article_by_category tag requires 1 argument: 'category_slug'"

    return GetArticleByCategory(category_slug)