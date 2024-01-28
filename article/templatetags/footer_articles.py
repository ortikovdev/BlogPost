# from django import template
# from article.models import Article
# register = template.Library()
#
# @register.simple_tag
# def last_two_article(article):
#     return Article.objects.order_by('-id')[:2]