# -*- coding: utf-8 -*-

from scrapy.spiders import Spider


class GarrysmodSpider(Spider):
    name = 'garrysmod'
    allowed_domains = ['wiki.garrysmod.com']
    start_urls = ['https://wiki.garrysmod.com/navbar/']

    def parse_nav(self, response):
        ''' Parse the navigation bar list for our individual API components. '''

    parse = parse_nav

    def parse_hook(self, response):
        ''' Handles creating a Hook definition and its attributes. '''

    def parse_library(self, response):
        ''' Handles creating a Library definition and its subroutines. '''

    def parse_class(self, response):
        ''' Handles creating a Class definition and its methods/attributes. '''

    def parse_dpanel(self, response):
        ''' Hand;es creating a DPanel subclass and its methods/attributes. '''

    def parse_attribute(self, response, component, last_attr=False):
        ''' Handles parsing a component's method or attribute page. '''
