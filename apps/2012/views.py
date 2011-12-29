#coding=utf-8
from __future__ import with_statement
from uliweb import expose
from uliweb.orm import get_model
from uliweb import request



@expose('/2012/')
def index():
    settings.LAYOUT.SUBTITLE = '首页'
    return {} #'<h1>Hello, Uliweb</h1>'

@expose('/2012')
class siteView(object):
        
    def about(self):
        settings.LAYOUT.SUBTITLE = '关于大会'
        return dict(page=dict(pagename='about',cndata='')) 
    
    def schedule(self):
        settings.LAYOUT.SUBTITLE = '日程安排'
        return dict(page=dict(pagename='schedule',cndata=''))
    
    def collections(self):
        settings.LAYOUT.SUBTITLE = '大会集锦'
        return dict(page=dict(pagename='collections',cndata=''))    

    def registration(self):
        settings.LAYOUT.SUBTITLE = '报名注册'
        return dict(page=dict(pagename='registration',cndata=''))
        
    def sponsors(self):
        settings.LAYOUT.SUBTITLE = '支持单位'
        return dict(page=dict(pagename='sponsors',cndata=''))

    def volunteer(self):
        settings.LAYOUT.SUBTITLE = '志愿者'
        return dict(page=dict(pagename='volunteer',cndata=''))
    def venue(self):
        settings.LAYOUT.SUBTITLE = '会场交通'
        return dict(page=dict(pagename='venue',cndata=''))    
