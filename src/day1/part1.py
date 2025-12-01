EXAMPLE_INPUT_PATH = './inputs/day1/part1_example.txt'
INPUT_PATH = './inputs/day1/part1.txt'

def main() -> None:
    with open(INPUT_PATH, 'r') as input_text:
        commands: list[str] = input_text.readlines()
    
    total_zero_count = 0
    dial: int = 50
    for command in commands:
        direction = command[0]
        if direction == 'R':
            dial = (dial + int(command[1:])) % 100
        elif direction == 'L':
            dial = (dial - int(command[1:])) % 100
        
        if dial == 0: total_zero_count += 1
    print(total_zero_count)

if __name__ == '__main__':
    main()