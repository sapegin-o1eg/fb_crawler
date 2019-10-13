import os
from os.path import join, dirname
from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from facebookscraper import settings
from facebookscraper.spiders.fb import FbSpider

do_env = join(dirname(__file__), '.env')
load_dotenv(do_env)

FACEBOOK_LOGIN = os.getenv('FACEBOOK_LOGIN')
FACEBOOK_PWD = os.getenv('FACEBOOK_PWD')

if __name__ == '__main__':
    target_users = ['100008193704935', 'artem.kotelevich.3']
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(FbSpider, FACEBOOK_LOGIN, FACEBOOK_PWD, target_users)
    process.start()
