from graduate_info.proxies.jl_ip_proxy import JLIPProxy
import logging

class ProxyMiddleware:
    def __init__(self):
        self.proxy = JLIPProxy()
        self.logger = logging.getLogger(__name__)

    def process_request(self, request, spider):
        proxy = self.proxy.get_proxies('120000')
        if proxy:
            proxy_addr = proxy.get('http')
            request.meta['proxy'] = proxy_addr
            self.logger.info(f"Using dynamic proxy: {proxy_addr}")