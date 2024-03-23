def process_queries(queries):
    queue = []
    knights = []

    for query in queries:
        command = query.split()

        match command[0]:
            case "+":
                queue.append(int(command[1]))
            case "*":
                middle_position = len(queue) // 2 + len(queue) % 2
                queue.insert(middle_position, int(command[1]))
            case "!":
                queue.insert(0, int(command[1]))
            case "-":
                knights.append(queue.pop(0))

    return knights


def main():
    n = int(input())
    queries = [input() for _ in range(n)]

    knights = process_queries(queries)

    for knight in knights:
        print(knight)


if __name__ == "__main__":
    main()
