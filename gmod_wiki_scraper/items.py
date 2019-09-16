# -*- coding: utf-8 -*-

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose

from .processors import Join, Prefix, PrefixOne, Split, TextWrap


class ComponentItem(Item):
    # Unique id for this component, and the name and file we belong to.
    uuid = Field()
    name = Field()
    file = Field()

    # Identifier for our parent object.
    parent_uuid = Field()

    # Descriptive attributes.
    description = Field()


class AttributeItem(Item):
    # UUID of the parent component and attribute name.
    component_id = Field()
    name         = Field()

    # Does this method/attribute exist in the Menu, Client, or Server scope?
    is_menu   = Field()
    is_client = Field()
    is_server = Field()

    # Are we a function and do we have parameters?
    is_function = Field()
    parameters  = Field()


class ComponentLoader(ItemLoader):

    default_item_class = ComponentItem

    description_out = Compose(
        Split('\n'),
        TextWrap(77),
        Prefix('-- '),
        Join('\n'),
        PrefixOne('\n' + '-' * 80)
    )
