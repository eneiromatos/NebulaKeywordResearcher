from search_engines import SearchEngineSuggestions as SES
from file_writter import FileWriter as FW
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
    input('Press any/+ key to continue')
    sys.exit()
else:
    kw_getters = {'Google': SES.get_google,
                  'Bing': SES.get_bing,
                  'Yahoo': SES.get_yahoo,
                  #'Yandex US': SES.get_yandex_us, RANDOM JSON FORMAT SOMETIMES
                  'Ask': SES.get_ask,
                  'DuckDuckGo': SES.get_duckduckgo,
                  'Ecosia': SES.get_ecosia,
                  'Brave': SES.get_brave
                  }

    input_kws = [kw.strip('\n').strip() for kw in seed_kws.readlines() if kw not in ('', ' ', '\n', None)]

    print(f'{len(input_kws)} keywords will be scanned against {len(kw_getters)} search engines.\n'
          f'This process may take some time, please be patient.\n')
    input('Press any key to continue\n')

    for kw in input_kws:
        kws = tuple()
        for letter in ascii_lowercase[0]:
            new_kw = f'{kw} {letter}'
            for se, getter in kw_getters.items():
                print(f'Exploring for {new_kw} in {se}')
                kw_ses = SES.kw_results(getter, new_kw)
                kws += kw_ses
                print(kw_ses)
                print(f'{len(kw_ses)} keywords found in this step.\n')
        FW.write_txt(kws)
    with open(config.output_file, encoding='utf-8') as out_f:
        print(f'File {config.output_file} has been created, '
              f'{len(out_f.readlines())} unique keywords found.')

