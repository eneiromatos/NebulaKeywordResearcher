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


from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

user_agent = config.get('Network and Connection', 'user_agent')
timeout = config.getint('Network and Connection', 'timeout')

input_file = config.get('Working Files', 'input_keywords')
output_file = config.get('Working Files', 'output_keywords')
log_file = config.get('Working Files', 'log_file')
