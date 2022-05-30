"""
3) Для access.log должна собираться следующая информация:
 + общее количество строк wc -l < access.log - общее количество выполненных запросов
 + количество запросов по HTTP-методам: GET - 20, POST - 10 и т.п.
 + топ 3 IP адресов, с которых были сделаны запросы
 - топ 3 самых долгих запросов, должно быть видно метод, url, ip, длительность, дату и время запроса

4) Собранная статистика должна быть сохранена в json файл и выведена в терминал в следующем формате

5) Должен быть README.md файл, который описывает как работает скрипт
"""
import argparse
import re
import json
import os
from collections import defaultdict


def parse():
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
    return parser.parse_args()


def dir_to_files(my_path):
    return next(os.walk(my_path), (None, None, []))[2]


def main(args):
    dict_ip = defaultdict(
        lambda: {"ALL": 0, "GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
    method_dict = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
    longest_request = defaultdict(
        lambda: {"ip": '', "method": '', "url": '', "datetime": ''})
    # del my_dict[sorted(my_dict)[3]]
    with open(args.file) as lines:
        idx = 1
        for line in lines:
            if idx > 9:
                break
            print('\n', line)

            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            if ip_match is not None:
                ip = ip_match.group()
                dict_ip[ip]['ALL'] += 1

                method = re.search(r'] "(POST|GET|PUT|DELETE|HEAD)', line)
                if method is not None:
                    dict_ip[ip][method.group(1)] += 1
                    method_dict[method.group(1)] += 1

                    duration = re.search(r'" \d{4,5}', line)
                    longest_request[0]
                    if duration is not None and duration.group() > sorted(longest_request)[0]:
                        longest_request[duration]["ip"] = ip
                        longest_request[duration]["method"] = method.group(1)
                        url = re.search(r'\Bhttp://\B')
                        print(url)
                        longest_request[duration]["url"] = url

                idx += 1
    print(idx)
    print('\n', method_dict, '\n')
    print(json.dumps(dict_ip, indent=4))


if __name__ == "__main__":
    result_of_parsing = parse()
    if os.path.isdir(str(result_of_parsing)):
        files = dir_to_files(result_of_parsing)
        for file in files:
            main(file)
    else:
        main(result_of_parsing)
