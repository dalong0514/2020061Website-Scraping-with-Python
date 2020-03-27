# -*- coding: utf-8 -*-

BOT_NAME = 'sainsburys'

SPIDER_MODULES = ['sainsburys.spiders']
NEWSPIDER_MODULE = 'sainsburys.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'

FEED_EXPORT_ENCODING = 'utf-8'

CONCURRENT_REQUESTS = 1

ITEM_PIPELINES = {
    'sainsburys.pipelines.DuplicateItemFilter': 1,
    'sainsburys.pipelines.CsvItemPipeline': None,
}

FEED_EXPORTERS = {
    'mycsv': 'sainsburys.exporters.CsvItemExporter'
}

LOG_FORMATTER = 'sainsburys.formatter.SilentlyDroppedFormatter'

DOWNLOADER_MIDDLEWARES = {
    'sainsburys.middlewares.SainsburysDownloaderMiddleware': 777
}
