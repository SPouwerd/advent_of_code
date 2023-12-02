number_strings: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def part_1(lines: list[str]):
    result: int = 0

    for line in lines:
        numbers: list[str] = []

        for character in line:
            if character.isnumeric():
                numbers.append(character)

        result += int(numbers[0] + numbers[-1])

    return result


def part_2(lines: list[str]):
    result: int = 0

    for line in lines:
        numbers: list[str] = []
        possible_number: str = ""

        for character in line:
            if character.isalpha():
                possible_number += character

                for number in number_strings:
                    if number in possible_number:
                        numbers.append(str(number_strings.index(number) + 1))
                        possible_number = possible_number[-1:]

            if character.isnumeric():
                numbers.append(character)
                possible_number = ""

        result += int(numbers[0] + numbers[-1])

    return result


with open("2023/data/day_1.txt", mode="r") as file:
    lines = file.readlines()
    striped_lines = [x.strip() for x in lines]

    result_1 = part_1(striped_lines)
    print(f"Result part 1: \n{result_1}")

    result_2 = part_2(striped_lines)
    print(f"Result part 2: \n{result_2}")
