# Formatter (NAME TBD)

## Goals:

- Make your code as short as possible.
- Retain near identical functionality.

## Authors/Maintainers:

- Sawbez
- brodycritchlow

## How this works:

1. Your code is parsed into an AST
2. We run through the AST, converting each node to text.
3. When all nodes are done, we are finished.

## Credits:

Credit to `astor`, which this formatter
is built on.
