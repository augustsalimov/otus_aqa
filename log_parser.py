import argparse
import re
import json
import os
from collections import defaultdict


def parse():
    # parsing argument from cli
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
    return parser.parse_args()


def dir_to_files(my_path):
    # return couple files in dir
    return next(os.walk(my_path), (None, None, []))[2]


def main(args):
    amount_of_lines = 0
    # ip: number of uses
    ip_dict = defaultdict(lambda: 0)
    # methods: amount of uses
    method_dict = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}

    longest_request = defaultdict(
        lambda: {"ip": '', "method": '', "url": '', "datetime": ''})
    request = {"ip": '', "method": '', "url": '', "datetime": '', "duration": ''}
    list_of_longest_requests = []
    # supportive list
    support = [0, 0, 0]

    with open(args.file) as lines:
        for line in lines:
            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            if ip_match is not None:
                ip = ip_match.group()
                ip_dict[ip] += 1

                method = re.search(r'] "(POST|GET|PUT|DELETE|HEAD)', line)
                if method is not None:
                    method = method.group(1)
                    method_dict[method] += 1

                    duration = re.search(r'" \d{4,5}', line)

                    if duration is not None:
                        duration = int(duration.group()[2:])
                        if duration > support[0]:
                            datetime = \
                                re.search(r'\d{1,2}/\w{2,4}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{1,4}', line).group()
                            request["ip"] = ip
                            request["method"] = method
                            request["datetime"] = datetime
                            request["duration"] = duration

                            list_of_longest_requests.append(request)

                            if len(list_of_longest_requests) > 3:
                                del list_of_longest_requests[0]
                            support[0] = duration
                            support = sorted(support)
                amount_of_lines += 1

    # ip dict to top ip dict
    ip_dict = {k: v for k, v in sorted(ip_dict.items(), key=lambda item: item[1])}
    support = sorted({v: k for k, v in ip_dict.items()}, reverse=True)[:3]
    top_ip = {k: v for k, v in ip_dict.items() if v in support}

    return {"top_ips": top_ip, "top_longest": list_of_longest_requests, "total_stat": method_dict, "total_requests": amount_of_lines}


def output(json_):
    with open('json_file.json', 'w', encoding='utf-8') as f:
        json.dump(json_, f, indent=4)
    print(json.dumps(json_, indent=4))


if __name__ == "__main__":
    result_of_parsing = parse()
    out = ''
    if os.path.isdir(str(result_of_parsing)):
        files = dir_to_files(result_of_parsing)
        for file in files:
            out = main(file)
    else:
        out = main(result_of_parsing)
    output(out)
