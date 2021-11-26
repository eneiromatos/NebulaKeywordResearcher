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


import config
import time


class FileWriter:

    @staticmethod
    def write_txt(kws: tuple[str]):
        with open(config.output_file, mode='a', encoding='utf-8') as kws_file:
            unique_kws = set(kws)
            ord_kws = [f'{kw}\n' for kw in unique_kws]
            ord_kws.sort()
            kws_file.writelines(ord_kws)

    @staticmethod
    def write_log(error: str):
        with open(config.log_file, mode='a') as log:
            log.write(f'{time.ctime(time.time())}:\n'
                      f'Error: {error}\n\n')
