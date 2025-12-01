EXAMPLE_INPUT_PATH = './inputs/day1/part2_example.txt'
INPUT_PATH = './inputs/day1/part2.txt'

def main() -> None:
    with open(EXAMPLE_INPUT_PATH, 'r') as input_text:
        commands: list[str] = input_text.readlines()
    
    total_zero_count = 0
    dial: int = 50
    for command in commands:
        direction: str = command[0]
        click_count: int = int(command[1:])
        if direction == 'R':
            dial_plus_count: int = dial + click_count
            while dial_plus_count >= 100:
                dial_plus_count -= 100
                total_zero_count += 1
            dial = dial_plus_count
        elif direction == 'L':
            dial_plus_count: int = dial - click_count
            while dial_plus_count <= 0:
                dial_plus_count += 100
                total_zero_count += 1
            dial = dial_plus_count
        print(dial, total_zero_count)
    print(total_zero_count)

if __name__ == '__main__':
    main()