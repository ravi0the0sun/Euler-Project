
# Euler Test Rig - Dev Specs

## General

- Use idomatic / build-in python testing where possible


## Folder structure

- Should allow custom folder structure, via config file, ideally TOML
- Should auto-generate a config file if not provided
- Config should provide paths to the folders for:
  - solutions
  - inputs
  - answers

### Solution Folder / Files

- Rig should read user created solutions from a solutions folder and test them
- Solution files must contain 4 digits representing the problem number
- Solution files should end in .py
- Solution files may contain extra filename before the 4 digits, eg.:
  - 0008.py
  - solution0008.py
  - s0008.py
- Solution files may contain extra filename after the 4 digits and before the extension, eg.:
  - 0008v2.py
  - 0008-brute-force.py
- Solution files should contain a solution function that takes a string input as only parameter and returns a string ouput

### Input Folder / Files

- When detecting a solution file the rig should look for an associated input file to pass in as input
- Input files should be in plain text files with no extension as provided by project euler
- Input files should be named with the problem number matching the solution in the solution folder. eg.:
  - 0004
  - 0008
  - 0134
- If an input file is found, it should be read to a string and provided to the solution as the only argument when testing
- If no input file is found, then `None` should be provided to the solution

### Answer Folder / Files

- Answer files should be read for the matching solution file and used to check answers when testing
- Answer files should be text files with no extension and only the problem number as the name:
  - 0005
  - 0010
  - 0016


## Nice to have

- Metadata keywords associated with solutions, eg. `slow`, `in-development`.
- Solution filtering:
  - Run only a specific solution
  - Run only a specific solution number
  - Run only solutions with specific keyword(s)
  - Run only solutions without specific keyword(s)
