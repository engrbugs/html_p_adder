#! /usr/bin/env python


def main():
    print('hello world')
    f = open("input.txt", "r")
    if f.mode == 'r':
        contents = f.read()
    print(contents)


if __name__ == "__main__":
    main()
