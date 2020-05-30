#! /usr/bin/env python


# Variable
input_txt_filename = 'input.txt'
output_txt_filename = 'output.txt'
add_string_before = '<p>'
add_string_after = '</p>'
trigger_character = '.'
# the Left of the triggered character must be numeric

def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]


def read_txt_file(filename):
    f = open(filename, "r")
    if f.mode == 'r':
        return f.read()
    f.close()


def write_txt_file(body):
    f = open(output_txt_filename, "w+")
    f.write(body)
    f.close()


def main():
    print('html adder by engrbugs')
    contents = read_txt_file(input_txt_filename)
    result = add_string_before + '\n'
    firstline = True  # <--- Don't add string in the first line.
    for line in contents.splitlines():
        x = line.find(trigger_character)
        if x is not -1:
            if left(line, x).strip().isnumeric():
                if not firstline:
                    result += add_string_before + '\n'
                    result += add_string_after + '\n'
        result += '\t' + line + '\n'
        firstline = None

    result += add_string_after
    print(result)
    write_txt_file(result)


if __name__ == "__main__":
    main()
