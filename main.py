import time

from search_engines import SearchEngineSuggestions as ses
from file_writter import FileWriter
from string import ascii_lowercase
import config
import sys

try:
    seed_kws = open(config.input_file, encoding='utf-8')
except FileNotFoundError:
    open(config.input_file, mode='w', encoding='utf-8')
    print(f'The file {config.input_file} has been created.\n'
          f'Proceed as follow:\n'
          f'\t1. Put your initial keyword there, one per line.\n'
          f'\t2. Pun this file again to scrape new keywords.\n')
    print('Press any key to continue')
    sys.exit()
else:
    kws = ()
    for kw in seed_kws.readlines():
        kw = kw.strip().strip('\n')
        if kw in ('', ' ', None):
            continue
        for letter in ascii_lowercase:
            new_kw = f'{kw} {letter}'
            
            print(f'Exploring for {new_kw} in Google')
            kw_google = ses.get_google(new_kw)
            if len(kw_google) > 0:
                if kw_google[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_google[1]}\n\n')
                else:
                    kws = kws + kw_google

            print(f'Exploring for {new_kw} in Bing')
            kw_bing = ses.get_bing(new_kw)
            if len(kw_bing) > 0:
                if kw_bing[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_bing[1]}\n\n')
                else:
                    kws = kws + kw_bing

            print(f'Exploring for {new_kw} in Yahoo')
            kw_yahoo = ses.get_yahoo(new_kw)
            if len(kw_yahoo) > 0:
                if kw_yahoo[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_yahoo[1]}\n\n')
                else:
                    kws = kws + kw_yahoo

            print(f'Exploring for {new_kw} in Yandex')
            kw_yandex_us = ses.get_yandex_us(new_kw)
            if len(kw_yandex_us) > 0:
                if kw_yandex_us[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_yandex_us[1]}\n\n')
                else:
                    kws = kws + kw_yandex_us

            print(f'Exploring for {new_kw} in Ask')
            kw_ask = ses.get_ask(new_kw)
            if len(kw_ask) > 0:
                if kw_ask[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_ask[1]}\n\n')
                else:
                    kws = kws + kw_ask

            print(f'Exploring for {new_kw} in DuckDuckGo')
            kw_duckduckgo = ses.get_duckduckgo(new_kw)
            if len(kw_duckduckgo) > 0:
                if kw_duckduckgo[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_duckduckgo[1]}\n\n')
                else:
                    kws = kws + kw_duckduckgo

            print(f'Exploring for {new_kw} in Ecosia')
            kw_ecosia = ses.get_ecosia(new_kw)
            if len(kw_ecosia) > 0:
                if kw_ecosia[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_ecosia[1]}\n\n')
                else:
                    kws = kws + kw_ecosia

            print(f'Exploring for {new_kw} in Brave')
            kw_brave = ses.get_brave(new_kw)
            if len(kw_brave) > 0:
                if kw_brave[0] is False:
                    with open(config.log_file, mode='a') as log:
                        log.write(f'{time.ctime(time.time())}:\n'
                                  f'Error: {kw_brave[1]}\n\n')
                else:
                    kws = kws + kw_brave

    FileWriter.write_txt(kws)
