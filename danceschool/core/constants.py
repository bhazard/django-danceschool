from django.db import connection
from django.utils.translation import ugettext_lazy as _

from dynamic_preferences.registries import global_preferences_registry
from .utils.sys import isPreliminaryRun


def getConstant(name):
    '''
    This is a convenience function that makes it easy to access the value of a preference/constant
    without needing to check if the django_dynamic_preferences app has been set up and without
    needing to load from that model directly.
    '''

    # We instantiate a manager for our global preferences
    if 'dynamic_preferences_globalpreferencemodel' in connection.introspection.table_names() and not isPreliminaryRun():
        params = global_preferences_registry.manager()
        try:
            return params.get(name)
        except:
            return None


def updateConstant(name,value,fail_silently=False):
    '''
    This is a convenience function that makes it easy to update the value of a preference/constant
    without needing to check if the django_dynamic_preferences app has been set up, without
    needing to load from that model directly, and with the option to suppress any errors
    (e.g. KeyErrors resulting from the order in which apps are loaded).
    '''

    # We instantiate a manager for our global preferences
    if 'dynamic_preferences_globalpreferencemodel' in connection.introspection.table_names() and not isPreliminaryRun():
        params = global_preferences_registry.manager()
        try:
            params[name] = value
            return True
        except:
            if not fail_silently:
                raise
            return False


HOW_HEARD_CHOICES = [
    ('','------'),
    ('Previous Student',_('I\'ve Taken Classes Before')),
    ('Facebook',_('Facebook')),
    ('Flyers',_('Flyers/Cards')),
    ('Friend',_('Another Student')),
    ('Other',_('Other')),
]
