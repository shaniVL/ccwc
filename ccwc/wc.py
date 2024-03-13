import click
import sys

def byte_count(lines: list[str]):
    count = len(lines)
    for line in lines:
        count += len(line.encode("utf-8"))
    return count

def line_count(lines: list[str]):
    return len(lines)

def word_count(lines: list[str]):
    count = 0
    for line in lines:
        count += len(line.strip().split())
    return count

def char_count(lines: list[str]):
    count = len(lines)
    for line in lines:
        count += len(line)
    return count

@click.command()
@click.option('-l', is_flag=True, default=False, help="Prints the line count")
@click.option('-c', is_flag=True, default=False, help="Prints the byte count")
@click.option('-w', is_flag=True, default=False, help="Prints the word count")
@click.option('-m', is_flag=True, default=False, help="Prints the char count")
@click.argument('filename', type=click.Path(exists=True), required=False)
def wc(l, w, c, m, filename):
    if not sys.stdin.isatty():
        lines = click.get_text_stream('stdin').readlines()
        identifier = ""
    else:
        lines = click.open_file(filename).readlines()
        identifier = filename
    
    if l:
        click.echo(f"{line_count(lines)} {identifier}")
    elif c:
        click.echo(f"{byte_count(lines)} {identifier}")
    elif w:
        click.echo(f"{word_count(lines)} {identifier}")
    elif m:
        click.echo(f"{char_count(lines)} {identifier}")
    else:
        click.echo(f"  {line_count(lines)}  {word_count(lines)} {byte_count(lines)} {identifier}")
        
if __name__ == "__main__":
    wc()
