# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from uuid import uuid4

from ..items import ComponentItem


class GarrysmodSpider(Spider):
    name = 'garrysmod'
    allowed_domains = ['wiki.garrysmod.com']
    start_urls = ['https://wiki.garrysmod.com/navbar/']
    state = {}

    def parse_nav(self, response):
        ''' Parse the navigation bar list for our individual API components. '''

        # First yield our global component, and pass it's id on to all child requests.
        #  *This ensures that anything can be linked to the global scope.*
        global_uuid = uuid4()
        global_item = ComponentItem(
            uuid=global_uuid,
            name='global',
            file='global.lua'
        )
        yield global_item

        category_list = response.xpath('/html/body/ul[1]/li')
        for category in category_list:
            category_name = (category.xpath('./h1/text()').get() or '').casefold()

            if category_name not in self._category_parsers:
                continue

            component_list = category.xpath('./ul[1]/li')
            for component in component_list:
                link = component.xpath('./h2/a')
                if link.attrib.get('href'):
                    yield response.follow(link.attrib['href'],
                                          callback=self._category_parsers[category_name],
                                          priority=self._category_priority[category_name],
                                          meta={'global': global_uuid}
                                          )

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

    _category_parsers = {
        'hooks':     parse_hook,
        'libraries': parse_library,
        'global':    parse_attribute,
        'classes':   parse_class,
        'panels':    parse_dpanel
    }
    _category_priority = {
        'hooks':     1,
        'libraries': 3,
        'global':    5,
        'classes':   7,
        'panels':    9
    }
