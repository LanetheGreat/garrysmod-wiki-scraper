# -*- coding: utf-8 -*-

from scrapy import Field, Item


class ComponentItem(Item):
    uuid = Field()


class AttributeItem(Item):
    component = Field()
