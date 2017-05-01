from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

    #creating class variables/static variables (shared by all instances)
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = set()
    crawled = set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.base_url=base_url
        Spider.project_name=project_name
        Spider.domain_name=domain_name
        Spider.queue_file=project_name+'/queue.txt'
        Spider.crawled_file=project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)