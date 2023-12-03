max_cubes = {"green": 13, "red": 12, "blue": 14}


def part_1(games: list[list[str]]) -> int:
    result = 0

    for game_index, bags in enumerate(games, start=1):
        if all(is_bag_valid(bag) for bag in bags):
            result += game_index

    return result


def is_bag_valid(bag: str) -> bool:
    colors_in_bag: dict[str, int] = {}

    for cubes in bag.split(", "):
        count, color = cubes.strip().split(" ")
        count = int(count)

        if color in colors_in_bag:
            colors_in_bag[color] += count
        else:
            colors_in_bag[color] = count

    return all(
        colors_in_bag.get(color, 0) <= max_cubes[color] for color in colors_in_bag
    )


def part_2(lines: list[str]):
    pass


with open("2023/data/day_2.txt", mode="r") as file:
    lines = file.readlines()
    striped_lines = [x.split(":")[1].strip() for x in lines]
    games = [line.split(";") for line in striped_lines]

    result_1 = part_1(games)
    print(f"Result part 1: \n{result_1}")

    # result_2 = part_2(striped_lines)
    # print(f"Result part 2: \n{result_2}")
