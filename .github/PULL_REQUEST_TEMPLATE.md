## Description

Please provide a brief description of the changes you are proposing, including any relevant context. If applicable, describe any problems you encountered and how you addressed them.

## What this completes

- [ ] Removed extra newline after statements with a single thing in their body (e.g. `if x:b` instead of `if x:<NEWLINE>b`)
- [ ] Prevent extra new lines (particularly for things in parentheses)
- [ ] Remove any spaces around parentheses
- [ ] Replace all possible newlines with `;`. This will likely require extended AST analysis (could be *future* category)
- [ ] Remove spacing around string literals if possible
- [ ] Merge imports into one line
- [ ] Remove type annotations
- [ ] Rename all variables to `a`, `b`, `c`, etc. (This *could* be implemented in Formatting, but likely *shouldn't*)
- [ ] Assign builtins used multiple times to a variable (e.g. `a, b = range(5), range(3)` becomes `r=range;a,b=r(5),r(3)`)
- [ ] **⚠ BLOCKER: Add the ability to manipulate the AST before converting**
- [ ] "Danger" Mode (allow certain shortens that might harm code execution)
  - [ ] Change all imports to star imports
  - [ ] Remove `assert` statements
- [ ] Switch to a custom AST-based converter with less limitations from SourceGenerator
  - [ ] This could also free us from the 3-Clause BSD if we wanted to use Unlicense or MIT

## Related Issues or PRs

If this pull request is related to any existing issues or pull requests, please provide links to them.

## Additional Notes

Please include any additional information or notes here that you think would be helpful for the reviewers of your pull request.
