#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/9

def get_input_file(file_path):
    """read input file and return a list of port outputs

    :param file_path: file path to input file --> str
    :rtype: list
    """
    with open(file_path) as f:
        port_output = [int(line.strip()) for line in f]
    return port_output


def is_invalid_number(start_index, end_index, port_output):
    """return True if a number cannot be represented as a sum of 
       previous pair of different numbers

    :param start_index: start of the preamble
    :param end_index: end of the preamble
    :param port_output: list of the input port outputs
    :rtype: bool
    """
    for i in port_output[start_index:end_index]:
        for j in port_output[start_index:end_index]:
            if i == j: continue
            if i + j == port_output[end_index]: return False
    return True


def main():
    file_path = "input.txt"
    port_output = get_input_file(file_path)
    start_index = 0
    end_index = 25
    while True:
        if is_invalid_number(start_index, end_index, port_output):
            return port_output[end_index]
        start_index += 1
        end_index += 1
    

if __name__ == "__main__":
    first_invalid_number = main()
    print(f"{first_invalid_number}")
