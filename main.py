import json
import logging
import concurrent.futures
import random
import requests
import pandas as pd
import itertools
from sources import SOURCES

logging.basicConfig(
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

HEADERS = {
    'User-Agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.{random.randint(0, 9999)} Safari/537.{random.randint(0, 99)}'  # noqa
}
MAX_WORKERS = 300
AVAILABLE_PROXIES = []
USABLE_PROXIES = []


class ProxyItem:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.proxy = {
            'http': f'http://{self.ip}:{self.port}',
            'https': f'http://{self.ip}:{self.port}'
        }
        self.is_valid = self.check()
        result_check = self.is_valid
        if result_check == True:
            logging.info(f'Live: {self.ip}:{self.port}')

    def check(self) -> bool:
        global USABLE_PROXIES
        try:
            check = requests.get(
                url='https://ipecho.net/plain',
                proxies=self.proxy,
                timeout=10
            )
            ms = check.elapsed.total_seconds()
            USABLE_PROXIES.append({'ip': self.ip, 'port': self.port})
            return True
        except:
            return False


class Scraper:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.url: str = self.config.get('url')
        self.method: str = self.config.get('method')
        self.parser: dict = self.config.get('parser', {})
        self.parser_type: str = list(self.parser.keys())[0]
        self.parser_config: dict = list(self.parser.values())[0]
        self.request_timeout = 10
        self.is_succeed = False
        logging.info(f'Source: {self.config.get("id")} has started.')

    def crawl(self) -> requests.Response:
        return requests.request(
            method=self.method,
            url=self.url,
            headers=HEADERS,
            timeout=self.request_timeout
        )

    def parse(self) -> list:
        proxies = []

        try:
            response = self.crawl()
            if self.parser_type == "pandas":
                df = pd.read_html(response.content)[self.parser_config.get('table_index', 0)]
                for x in range(0, len(df)):
                    if not self.parser_config.get('combined', None):
                        ip = str(df.loc[df.index[x], self.parser_config.get('ip')]).strip()
                        port = int(df.loc[df.index[x], self.parser_config.get('port')])
                        proxies.append({'ip': ip, 'port': port})
                    else:
                        combined: str = df.loc[df.index[x], self.parser_config.get('combined')]
                        if len(combined.split(':')) == 2:
                            ip = combined.split(':')[0].strip()
                            port = int(combined.split(':')[1])
                            proxies.append({'ip': ip, 'port': port})

            if self.parser_type == "json":
                data = response.json()[self.parser_config.get('data')]
                for x in data:
                    proxies.append({
                        'ip': str(x[self.parser_config.get('ip', '')]).strip(),
                        'port': int(x[self.parser_config.get('port', '')])
                    })
            if self.parser_type == "json2":
                datass = response.text
                with open(f"data\\test.txt", 'w') as f:
                    f.write(f'{datass}')
                file1 = open('data\\test.txt', 'r')
                Lines = file1.readlines()
                count = 0
                for line in Lines:
                    count += 1
                    a=line.strip()
                    b=json.loads(a)
                    proxies.append({
                            'ip': str(b.get('host', '')),
                            'port': int(b.get('port', ''))
                        })


            if self.parser_type == "txt":
                data = str(response.content, encoding='utf-8')
                for x in data.split('\n'):
                    if len(x.split(':')) == 2:
                        proxies.append({
                            'ip': x.split(':')[0].strip(),
                            'port': int(x.split(':')[1].strip())
                        })
            self.is_succeed = True
        except:
            self.is_succeed = False
            logging.error(f'Source: {self.config.get("id")}', exc_info=True)

        return proxies

    def run(self) -> bool:
        global AVAILABLE_PROXIES
        proxies = self.parse()
        with open(f"data\\{self.config.get('id')}.json", "w") as f:
            f.write(f'{proxies}\n')
        with open(f"data_txt\\{self.config.get('id')}.txt", "w") as m:
            for proxys in proxies:
                conver_txt = f"{proxys['ip']}:{proxys['port']}"
                m.write(f'{conver_txt}\n')
        if len(proxies) > 0:
            AVAILABLE_PROXIES = itertools.chain(AVAILABLE_PROXIES, proxies)

        return self.is_succeed, len(proxies)


def geolocation_info(batch_ips) -> list:
    try:
        def batch_request(data):
            response = requests.post("http://ip-api.com/batch", json=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None

        batch_limit = 100
        ip_api_results = []
        list_of_ip = [x["ip"] for x in batch_ips]
        for start in range(0, len(list_of_ip), batch_limit):
            batch = list_of_ip[start: start + batch_limit]
            geo = batch_request(batch)
            if geo:
                ip_api_results = itertools.chain(ip_api_results, geo)

        proxy_dict = dict([(x["ip"], x["port"]) for x in batch_ips])
        model = []
        for x in list(ip_api_results):
            ip = x['query']
            port = proxy_dict[ip]
            model.append({"ip": ip, "port": port, "geolocation": x})

        return model
    except:
        return []


def main():
    global MAX_WORKERS
    source_states = []

    for config in SOURCES:
        scraper = Scraper(config)
        succeed, count = scraper.run()
        source_states.append({
            "id": config['id'],
            "url": config['url'],
            "succeed": succeed,
            "count": count
        })

    list_of_proxies = list(AVAILABLE_PROXIES)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        worker_to_queue = {
            executor.submit(ProxyItem, x['ip'], x['port']): x for x in list_of_proxies
        }
        for worker in concurrent.futures.as_completed(worker_to_queue):
            worker_to_queue[worker]

    with open("proxy-list/data.txt", "w") as f:
        for x in USABLE_PROXIES:
            f.write(f'{x.get("ip")}:{x.get("port")}\n')

    logging.info(f'{len(list_of_proxies)} proxies are crawled.')
    logging.info(f'{len(USABLE_PROXIES)} proxies are usable.')


if __name__ == '__main__':
    main()

