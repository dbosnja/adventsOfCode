#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/8 - part 1


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read()]


def main():
    file_path = "input.txt"
    input_encoding = get_input(file_path)
    width = 25
    height = 6
    image_size = width * height
    layers_no = int(len(input_encoding) / image_size)
    layers_map = {i: input_encoding[i * image_size:i * image_size + image_size]
                  for i in range(layers_no)}
    least_zeros = min({pixels.count(0) for pixels in layers_map.values()})
    req_layer = [layer for layer, pixels in layers_map.items()
                 if pixels.count(0) == least_zeros][0]
    return layers_map[req_layer].count(1) * layers_map[req_layer].count(2)


if __name__ == "__main__":
    print(f"{main()}")
