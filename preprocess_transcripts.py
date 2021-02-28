
import re


def remove_duplicate_blancos(filename):
    with open(filename) as r:
        text = re.sub(' +', ' ', r.read())
    with open(filename, "w") as w:
        w.write(text)


def remove_duplicate_whitespace(filename):
    with open(filename) as r:
        text = ' '.join(r.read().split())
    with open(filename, "w") as w:
        w.write(text)


if __name__ == '__main__':
    filename = 'Futurama_transcripts.txt'
    remove_duplicate_blancos(filename)
