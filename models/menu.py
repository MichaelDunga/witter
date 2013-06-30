# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = "Witter"
response.subtitle = "Super Awesome Twitter Clone in Web2Py"
response.menu = [
    (T('Home'), False, URL('default','home')),
    (T('Wall'), False, URL('default','wall')),
    (T('Search'), False, URL('default','search')),
    ]
