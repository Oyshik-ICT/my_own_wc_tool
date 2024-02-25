import click
import os
import sys

def read_file(file, mode):
    f = open(file[0], mode)
    fp = f.read()
    if mode == 'r':
        return f, fp
    else:
        return fp

@click.command()
@click.option(
    "-c",
    "file_bytes",
    is_flag = True,
    help = "Total size of input file is written to the output",
)
@click.option(
    "-l",
    "file_lines",
    is_flag = True,
    help = "Total lines of input file is written to the output",
)
@click.option(
    "-w",
    "file_words",
    is_flag = True,
    help = "Total words of input file is written to the output",
)
@click.option(
    "-m",
    "file_characters",
    is_flag = True,
    help = "Total characters of input file is written to the output",
)
@click.argument("file", nargs = -1, type = click.Path(exists=True))
def calculate(file_bytes, file_lines, file_words, file_characters, file):

    if len(file) != 0:
        f, fp = read_file(file, 'r')
        f.seek(0, os.SEEK_END)
        total_bytes = f.tell()
        fp = read_file(file, 'rb')
        total_chars = len(fp.decode("utf-8"))
        f.close()
    else:
        f = sys.stdin.buffer
        fp = f.read()
        total_bytes = len(fp)
        total_chars = len(fp.decode("utf-8"))
        f.close()


    total_lines = len(fp.splitlines())
    total_words = len(fp.split())

    if file_bytes:
        print(total_bytes)
    
    elif file_lines:
        print(total_lines)
    
    elif file_words:
        print(total_words)

    elif file_characters:
        print(total_chars)
    else:
        print(total_lines, total_words, total_bytes)
    
if __name__ == "__main__":
    calculate()