# -*- coding: utf-8 -*-

from scrapy import signals


class GModComponentPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        ''' Creates a pipeline instance and hooks in its signal handlers. '''
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_idle, signal=signals.spider_idle)
        return pipeline

    def process_item(self, item, spider):
        ''' Initializes components or links a component's attributes
            to itself in a spider's component cache. '''
        return item

    def spider_idle(self, spider):
        ''' Finalizes and serializes a spider's component cache once
            it's crawled the entire GMod wiki site. '''
        pass
