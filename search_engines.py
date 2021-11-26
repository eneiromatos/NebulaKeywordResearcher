'''
Nebula Keyword Researcher: is designed to scrape keywords from
major search engines like Google, Bing and Yahoo.

Copyright (C) 2021. Eneiro A. Matos B.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


import requests
import config
from file_writter import FileWriter as fw


class SearchEngineSuggestions:
    headers = {
        'user-agent': config.user_agent
    }

    @staticmethod
    def get_yahoo(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        n_results = 20
        try:
            html = requests.get(f'https://search.yahoo.com/sugg/gossip/gossip-us-ura/?'
                                f'command={kw}&output=json&nresults={n_results}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()['gossip']['results']
            return tuple([result['key'] for result in results])

    @staticmethod
    def get_ask(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        n_results = 20
        try:
            html = requests.get(f'https://amg-ss.ask.com/query?limit={n_results}&q={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            return tuple(html.json()[1])

    @staticmethod
    def get_yandex_us(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://yandex.com/suggest/suggest-ya.cgi?v=4&bemjson=0&part={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])

    @staticmethod
    def get_duckduckgo(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://duckduckgo.com/ac/?q={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple([sugg['phrase'] for sugg in results])

    @staticmethod
    def get_ecosia(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://ac.ecosia.org/?q={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results['suggestions'])

    @staticmethod
    def get_brave(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://search.brave.com/api/suggest?q={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])

    @staticmethod
    def get_google(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://www.google.com/complete/search?q={kw}'
                                f'&client=firefox', headers=SearchEngineSuggestions.headers,
                                timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])

    @staticmethod
    def get_bing(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            # Got the API from https://stackoverflow.com/a/15318150
            html = requests.get(f'https://api.bing.com/osjson.aspx?query={kw}',
                                headers=SearchEngineSuggestions.headers, timeout=config.timeout)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])

    @staticmethod
    def kw_results(search_engine, kw):
        kws_search_engine = search_engine(kw)
        if len(kws_search_engine) > 0:
            if kws_search_engine[0] is False:
                fw.write_log(kws_search_engine[1])
                return tuple()
            else:
                return kws_search_engine
        else:
            return tuple()
