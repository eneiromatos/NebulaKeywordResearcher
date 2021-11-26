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
    input('Press any key to exit')
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

    if len(input_kws) == 0:
        print(f'Please insert at least one keyword in {config.input_file} to start, and try again.')
        input('Press any key to exit')
        sys.exit()

    print(f'{len(input_kws)} keywords will be scanned against {len(kw_getters)} search engines.\n'
          f'This process may take some time, please be patient.\n')
    input('Press any key to continue\n')

    for kw in input_kws:
        kws = tuple()
        for letter in ascii_lowercase:
            new_kw = f'{kw} {letter}'
            for se, getter in kw_getters.items():
                print(f'Exploring for {new_kw} in {se}')
                kw_ses = SES.kw_results(getter, new_kw)
                kws += kw_ses
                print(f'{len(kw_ses)} keywords found in this step.\n')
        FW.write_txt(kws)
    with open(config.output_file, encoding='utf-8') as out_f:
        print(f'File {config.output_file} has been created, '
              f'{len(out_f.readlines())} unique keywords found.')

