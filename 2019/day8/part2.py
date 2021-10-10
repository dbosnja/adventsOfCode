#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/8


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read()]


def create_image(pixels, width, height):
    return [pixels[h * width:h * width + width] for h in range(height)]


def main():
    file_path = "input.txt"
    input_encoding = get_input(file_path)
    width = 25
    height = 6
    image_size = width * height
    layers_no = int(len(input_encoding) / image_size)
    layers_map = {i: input_encoding[i * image_size:i * image_size + image_size]
                  for i in range(layers_no)}
    layers_map = {i: create_image(layers_map[i], width, height)
                  for i in layers_map}
    final_image = []
    for h in range(height):
        for w in range(width):
            for i in layers_map:
                if layers_map[i][h][w] in (0, 1):
                    final_image.append(layers_map[i][h][w])
                    break

    height = int(len(final_image) / width)
    message = create_image(final_image, width, height)
    for row in message:
        for pixel in row:
            if pixel:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
