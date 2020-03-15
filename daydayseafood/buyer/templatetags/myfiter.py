from django.template import Library

register = Library()


def getlist5(params: list):
    return params[0:5]
