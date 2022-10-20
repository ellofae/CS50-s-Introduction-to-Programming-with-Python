def main():
    #hello() - prints 'hello, no name'
    name = input("What's your name? ").strip().title()
    hello(name)


def hello(fullName="no name"):
    print(f"hello, {fullName}")

main()