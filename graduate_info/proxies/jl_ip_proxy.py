# coding=utf-8
""" 巨量ip proxy"""

import hashlib
from dotenv import load_dotenv
import os
from typing import Optional

import requests
from scrapy.crawler import logger

from graduate_info.proxies.ip_proxy import IpProxy

load_dotenv()


class SignKit:
    post_charset = "UTF-8"
    file_charset = "UTF-8"

    @staticmethod
    def md5_sign(params, secret: str) -> str:
        return SignKit.md5(SignKit.get_sign_content(params) + '&key=' + secret)

    @staticmethod
    def get_sign_content(params):
        params.pop('sign', None)
        sorted_params = sorted(params.items())
        string_to_be_signed = ''
        for k, v in sorted_params:
            if not SignKit.check_empty(v) and not v.startswith('@'):
                v = SignKit.character(v, SignKit.post_charset)
                if not string_to_be_signed:
                    string_to_be_signed += f'{k}={v}'
                else:
                    string_to_be_signed += f'&{k}={v}'
        return string_to_be_signed

    @staticmethod
    def character(data, target_charset):
        if not SignKit.check_empty(data):
            file_type = SignKit.file_charset
            if file_type.lower() != target_charset.lower():
                return data.encode(target_charset).decode(target_charset)
        return data

    @staticmethod
    def check_empty(value):
        return value is None or value.strip() == ''

    @staticmethod
    def md5(input_str):
        return hashlib.md5(input_str.encode()).hexdigest()


class JLIPProxy(IpProxy):

    def __init__(self):
        self.trade_no = os.getenv("JU_LIANG_IP_API_KEY")
        self.api_key = os.getenv("JU_LIANG_IP_SECRET")
        self.base_url = "http://v2.api.juliangip.com/company/dynamic/getips"

    def get_dynamic_ip(self, area: str) -> Optional[str]:
        params = {
            'trade_no': self.trade_no,
            'num': '1',
            'pt': '1',
            'result_type': 'json'
        }
        # 计算签名
        sign = SignKit.md5_sign(params, self.api_key)
        params['sign'] = sign

        # 发起请求
        res = requests.get(self.base_url, params=params)

        logger.info(f"get ip result: {res.text}")
        if res.status_code != 200 or res.json().get("code") != 200:
            return None
        return res.json().get("data", {}).get("proxy_list", [])[0]


# 以下使用示例为提取【动态代理】，仅供参考
# 具体API参数说明请参照：https://www.juliangip.com/help/api/dynamic/
if __name__ == '__main__':
    target_url = "https://qifu.baidu.com/ip/local/geo/v1/district"
    kdl_ip_proxy = JLIPProxy()
    proxies = kdl_ip_proxy.get_proxies('120000')
    response = requests.get(target_url, proxies=proxies)
    print(f"target res {response.text}")
