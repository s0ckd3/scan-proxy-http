SOURCES = [
    {
        "id": "free-proxy-list.net",
        "url": "https://free-proxy-list.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "us-proxy.org",
        "url": "https://www.us-proxy.org",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxydb.net",
        "url": "http://proxydb.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": None,
                "port": None,
                "combined": "Proxy",
            },
        }
    },
    {
        "id": "free-proxy-list.com",
        "url": "https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 1,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxy-list.download",
        "url": "https://www.proxy-list.download/HTTP",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "vpnoverview.com",
        "url": "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "roosterkid_openproxylist",
        "url": "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "jetkai_proxy-list",
        "url": "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "proxyscrape.com",
        "url": "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "sunny9577_proxy-scraper",
        "url": "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "monosans_proxy-list",
        "url": "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "TheSpeedX_PROXY-List",
        "url": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "proxylists.net",
        "url": "http://www.proxylists.net/http_highanon.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "rdavydov_proxy-list",
        "url": "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "mmpx12_proxy-list",
        "url": "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "hendrikbgr_Free-Proxy-Repo",
        "url": "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "rx443_proxy-list",
        "url": "https://raw.githubusercontent.com/rx443/proxy-list/main/online/all.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "proxy4parsing_proxy-list",
        "url": "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "ReCaree_proxy-scrapper",
        "url": "https://raw.githubusercontent.com/ReCaree/proxy-scrapper/master/proxy/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "fate0_proxylist",
        "url": "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list",
        "method": "GET",
        "parser": {
            "json2": {},
        }
    }
]
