#-*- coding: utf-8 -*-

from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT,  'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)


#Con est se puede parametrizar el atributo desde afuera.
LICENSES = getattr(settings, 'LICENSES', 'DEFAULT_LICENSES')

BADWORDS = getattr(settings, 'PROJECT_BADWORDS', '')