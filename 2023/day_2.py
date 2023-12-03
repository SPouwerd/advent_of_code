max_cubes = {"green": 13, "red": 12, "blue": 14}


def is_bag_valid(bag: str):
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


def part_1(games: list[list[str]]):
    result = 0

    for game_index, bags in enumerate(games, start=1):
        if all(is_bag_valid(bag) for bag in bags):
            result += game_index

    return result


def part_2(games: list[list[str]]):
    result = 0
    valid_games: list[list[str]] = []

    for bags in games:
        if all(is_bag_valid(bag) for bag in bags):
            valid_games.append(bags)

    for bags in valid_games:
        print(bags)

    return result


with open("2023/data/day_2.txt", mode="r") as file:
    striped_lines = [x.split(":")[1].strip() for x in file.readlines()]
    games = [line.split(";") for line in striped_lines]

    result_1 = part_1(games)
    print(f"Result part 1: \n{result_1}")

    result_2 = part_2(games)
    print(f"Result part 2: \n{result_2}")
