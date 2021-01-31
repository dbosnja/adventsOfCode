from collections import defaultdict


def is_valid(policy, password):
    """ return 1 if password satisfies the policy. else 0

    :param policy: str
    :param password: str
    :rtype: int
    """
    req_range, char = map(str.strip, policy.split(' '))
    req_min, req_max = map(int, req_range.split('-'))
    char_counter = 0
    for c in password:
        if c == char:
            char_counter += 1
    return 1 if char_counter in range(req_min, req_max + 1) else 0

def get_web_data(file_path):
    """ preprocess data from a file containing policies and passwords

    :param file_path: path to a file containing data --> str
    :rtype: defauldict(list)
    """
    web_items = defaultdict(list)
    with open(file_path) as f:
        for line in f:
            policy, password = map(str.strip, line.split(':'))
            web_items[policy].append(password)
    return web_items


def main():
    file_path = '/home/dom-ak45/Desktop/pass.txt'
    valids_sum = 0
    for policy, passwords in get_web_data(file_path).items():
        for password in passwords:
            valids_sum += is_valid(policy, password)
    print(f"Number of valid passwords: {valids_sum}")


if __name__ == "__main__":
    main()
