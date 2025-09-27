import sys


def main():
    while True:
        user_input = input("$ ")
        command, *args = user_input.split(" ")

        match command:
            case "type":
                builtins = ["type", "echo", "exit"]
                if args[0] in builtins:
                    return print(f"{args[0]} is a shell builtin")
                else:
                    return print(f"{args[0]}: not found")
            case "echo":
                print(" ".join(args))
            case "exit":
                sys.exit(int(args[0]) if args else 0)
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
