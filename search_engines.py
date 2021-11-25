import requests
import config


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
                                headers=SearchEngineSuggestions.headers)
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
                                headers=SearchEngineSuggestions.headers)
        except Exception as e:
            return False, str(e)
        else:
            return tuple(html.json()[1])

    @staticmethod
    def get_yandex_us(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://yandex.com/suggest/suggest-ya.cgi?v=4&bemjson=0&part={kw}',
                                headers=SearchEngineSuggestions.headers)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()[1]
            return tuple([sugg for sugg in results if isinstance(sugg, str)])

    @staticmethod
    def get_duckduckgo(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            html = requests.get(f'https://duckduckgo.com/ac/?q={kw}',
                                headers=SearchEngineSuggestions.headers)
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
                                headers=SearchEngineSuggestions.headers)
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
                                headers=SearchEngineSuggestions.headers)
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
                                f'&client=firefox', headers=SearchEngineSuggestions.headers)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])

    @staticmethod
    def get_bing(kw: str) -> tuple[str] | tuple[bool, str]:
        kw = kw.casefold().replace(' ', '+')
        try:
            #Got the API from https://stackoverflow.com/a/15318150
            html = requests.get(f'https://api.bing.com/osjson.aspx?query={kw}',
                                headers=SearchEngineSuggestions.headers)
        except Exception as e:
            return False, str(e)
        else:
            results = html.json()
            return tuple(results[1])
