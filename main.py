from subprocess import run
from pathlib import Path


def capture_ps_aux():
    return run(["ps", "aux"], capture_output=True).stdout.decode('UTF-8')


def listing(text):
    text_split = text.split("\n")
    list_of_list = []
    for i in range(len(text_split)):
        list_of_list.append([j for j in text_split[i].split(" ") if j != ''])
    return list_of_list


def calculate(list_of_list):
    user_dict = {}
    num_of_process = 0
    max_cpu, max_mem = 0.0, 0.0
    performance = {'sum_cpu': 0.0, 'sum_mem': 0.0, 'max_cpu_command': [], 'max_mem_command': []}

    for i in range(1, len(list_of_list)-1):
        current_list = list_of_list[i]
        user = 0

        num_of_process += 1
        if current_list[user] not in user_dict:
            user_dict[current_list[user]] = 1
        else:
            user_dict[current_list[user]] += 1
        cur_cpu, cur_mem = current_list[2], current_list[3]

        if ',' in cur_cpu:
            cur_cpu, cur_mem = list(map(lambda x: x.replace(',', '.'), (cur_cpu, cur_mem)))
        cur_cpu, cur_mem = map(float, (cur_cpu, cur_mem))
        performance['sum_cpu'] += cur_cpu
        performance['sum_mem'] += cur_mem

        if cur_cpu > max_cpu:
            max_cpu = cur_cpu
            performance['max_cpu_command'] = current_list[10:]
        if cur_mem > max_mem:
            max_mem = cur_mem
            performance['max_mem_command'] = current_list[10:]

    users_processes = {k: v for k, v in reversed(sorted(user_dict.items(), key=lambda item: item[1]))}
    return users_processes, num_of_process, performance


def final_text_fun(users: dict, launched_process: int, performance: dict):
    users_of_system = ", ".join(f"'{key}'" for key in users.keys())
    processes = ''.join(f"\n{key}: {users[key]}" for key in users)
    sum_of_mem = f"{performance['sum_mem']:.1f}%"
    sum_of_cpu = f"{performance['sum_cpu']:.1f}%"
    max_mem_command = ''.join(performance['max_mem_command'])
    max_cpu_command = ''.join(performance['max_cpu_command'])

    text = \
        f"Отчёт о состоянии системы:\n\n" \
        f"Пользователи системы: {users_of_system}\nПроцессов запущено: {launched_process}\n" \
        f"Пользовательских процессов: {processes}\n" \
        f"Всего памяти используется: {sum_of_mem}\nВсего CPU используется: {sum_of_cpu}\n" \
        f"Больше всего памяти использует: {max_mem_command[:20]}\nБольше всего CPU использует: {max_cpu_command[:20]}"
    return text


def write_to_file(text):
    with open(Path('scan.txt'), 'w') as file:
        return file.write(text)


if __name__ == '__main__':
    result_of_capture = capture_ps_aux()
    result_of_listing = listing(result_of_capture)
    process_dict, num, performance_dict = calculate(result_of_listing)
    final_text = final_text_fun(process_dict, num, performance_dict)
    write_to_file(final_text)
    print(final_text)
