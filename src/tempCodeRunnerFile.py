gen = FormatterSourceGenerator(indent_with=' ')
ast_node = parse('if x: print(x)\nelse: print(x)')
gen.visit(ast_node)
print(''.join(gen.result))