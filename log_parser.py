import argparse
import re
import json
import os
from datetime import datetime
from collections import defaultdict


def parse():
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-p', dest='path', action='store', help='Path to logfile')
    args = parser.parse_args()
    return args.path


def dir_to_files(my_path):
    return os.listdir(my_path)


def main(path):
    amount_of_requests = 0
    ip_dict = defaultdict(lambda: 0)
    method_dict = {"GET": 0, "POST": 0, "HEAD": 0, "PUT": 0, "OPTIONS": 0, "DELETE": 0}
    list_of_longest_requests = []
    support = [0, 0, 0]

    with open(path) as lines:
        for line in lines:
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            method = re.search(r'] "(POST|GET|PUT|DELETE|HEAD|OPTIONS)', line)

            if ip and method is not None:
                ip = ip.group()
                ip_dict[ip] += 1
                method = method.group(1)
                method_dict[method] += 1

                try:
                    duration = re.search(r'\d{4,5}$', line)
                    duration = int(duration.group())

                    if duration > support[0]:
                        try:
                            datetime_ = re.search(r'\d{1,2}/\S*\s\+\d{1,4}', line).group()
                        except AttributeError:
                            datetime_ = ''
                        try:
                            url = re.search(r'http://\S*/', line).group()
                        except AttributeError:
                            url = ''

                        request = {"ip": ip, "method": method, "url": url, "datetime": datetime_, "duration": duration}
                        list_of_longest_requests.append(request)
                        support[0] = duration
                        support.sort()

                        if len(list_of_longest_requests) > 3:
                            del list_of_longest_requests[0]
                except AttributeError:
                    pass

                amount_of_requests += 1

    return {"top_ips": dict_to_top_dict(ip_dict), "top_longest": list_of_longest_requests,
            "total_stat": method_dict, "total_requests": amount_of_requests}


def output(json_):
    with open(f'json_file_{datetime.now()}.json', 'w', encoding='utf-8') as f:
        json.dump(json_, f, indent=4)
    print(json.dumps(json_, indent=4))


# helpers
def dict_to_top_dict(ip_dict):
    ip_dict = {k: v for k, v in sorted(ip_dict.items(), key=lambda item: item[1])}
    support = sorted({v: k for k, v in ip_dict.items()}, reverse=True)[:3]
    return {k: v for k, v in ip_dict.items() if v in support}


if __name__ == "__main__":
    path_ = parse()
    if os.path.isdir(path_):
        files = dir_to_files(path_)
        for file in files:
            file_path = os.path.join(path_, file)
            if os.path.isfile(file_path) and '.log' in file:
                output(main(file_path))
    else:
        output(main(path_)) if '.log' in path_ else print('Please choose log file')
