from abc import ABC, abstractmethod
from typing import Optional


class IpProxy(ABC):

    @abstractmethod
    def get_dynamic_ip(self, area: str) -> Optional[str]:
        pass

    def get_playwright_proxy(self, area: str):
        proxy_ip = self.get_dynamic_ip(area)
        if not proxy_ip:
            return None
        print(f"proxy ip: {proxy_ip}")
        return {
            "server": f"http://{proxy_ip}/",
        }

    def get_proxies(self, area: str):
        proxy_ip = self.get_dynamic_ip(area)
        if not proxy_ip:
            return None
        return {
            "http": f"http://{proxy_ip}/",
            "https": f"http://{proxy_ip}/"
        }
