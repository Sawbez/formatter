# TODO
**Contribute directly to this file if anything is mising!.**

### Formatting 🧹

- [ ] Prevent extra new lines (particularly for things in parentheses)
- [ ] Remove any spaces around parentheses
- [ ] Remove newline after statements with a single thing in their body (e.g. `if x:b` instead of `if x:<NEWLINE>b`)
- [ ] Replace all possible newlines with `;`. This will likely require extended AST analysis (could be *future* category).

### AST Manipulations 🛠
- [ ] **⚠ BLOCKER: Add the ability to manipulate the AST before converting**
- [ ] Merge imports into one line
- [ ] Remove type annotations
- [ ] Rename all variables to `a`, `b`, `c`, etc. (This *could* be implemented in Formatting, but likely *shouldn't*)
- [ ] Assign builtins used multiple times to a variable (e.g. `a, b = range(5), range(3)` becomes `r=range;a,b=r(5),r(3)`)

### Future Possibilites 🔮
- [ ] "Danger" Mode (allow certain shortens that might harm code execution)
  - [ ] Change all imports to star imports
  - [ ] Remove `assert` statements
- [ ] Switch to a custom AST-based converter with less limitations from SourceGenerator.
  - [ ] This could also free us from the 3-Clause BSD if we wanted to use Unlicense or MIT.

### Completed ✓
- [x] Basic space removals
- [x] README, TODO
