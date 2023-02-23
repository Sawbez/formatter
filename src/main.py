from ast import parse
from sys import argv

from astor import to_source
from formatter import FormatterSourceGenerator

with open(argv[1]) as f:
    text = f.read()
ast = parse(text)

source = to_source(
    ast, indent_with=" ", source_generator_class=FormatterSourceGenerator
)

print(source)
with open(argv[1][:-3] + "_new.py", "w") as f:
    f.write(source)

