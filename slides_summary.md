# Python Imports Tutorial Summary

## Core Concepts

### Import Processing Has Two Steps

- **Find** - Gain access to the module (uses `sys.path`)
- **Bind** - Give the module a name to use in code

### Import Resolution Order

1. Check if module is in `sys.modules` (cache) → use cached version
2. Check if it's in `sys.modules["builtins"]` → load built-in module
3. Search `sys.path` directories in order → load module via loader
4. If not found → raise `ModuleNotFoundError`

## sys.path is Critical

### REPL vs Script Differences

- **REPL**: First entry is `''` (current directory where REPL launched)
- **Running script**: First entry is location of the script file

### Standard sys.path Entries

- `/usr/lib/python314.zip` - Zipped standard library modules
- `/usr/lib/python3.14` - Unzipped standard library
- `/usr/lib/python3.14/lib-dynload` - Compiled C/C++ extensions
- `/usr/lib/python3.14/site-packages` - Third-party packages (pip installs)

### Key Rule

Python stops at the **first match** in `sys.path` order

## Shadowing Problem

If you create `datetime.py` in your project directory and it appears in `sys.path` before the standard library location, your file will "shadow" the standard library's datetime module.

## Modules vs Packages

### Module

- An object serving as an organizational unit of Python code (typically a `.py` file)
- Loaded via importing
- Has a namespace containing Python objects

### Package

- Directory structure used to organize modules
- Provides naming hierarchy
- **Regular packages**: require `__init__.py` file
- **Namespace packages**: no `__init__.py`, can span multiple directories (Python 3.3+)

### `__init__.py` Purpose

- Marks directory as a regular package
- Can be empty (most common)
- Can contain initialization code and imports
- Controls package's public API

## Absolute vs Relative Imports

### Absolute Imports

- Start from first entry in `sys.path`
- Work everywhere
- Recommended approach

### Relative Imports

- Use `.` and `..` syntax (like file paths)
- Only work within packages
- Fail when file is run as a script (not as module with `-m` flag)
- Use `-m` flag to run as module: `python3.14 -m one.sub2.mod2`

## Common Import Errors

### NameError

- Name not bound in namespace
- **Cause:** Missing import statement
- **Fix:** Add the import

### ImportError

- Module found but something inside can't be imported
- **Causes:** Misspelling, circular imports, structural issues
- **Fix:** Correct typos, resolve circular dependencies

### ModuleNotFoundError

- Subclass of ImportError
- Module itself cannot be found in `sys.path`
- **Cause:** Wrong path or module not in `sys.path`
- **Fix:** Adjust import path relative to first `sys.path` entry, or install missing package

## Lazy Imports

### Three Approaches

1. **Function-level imports** - Import inside function (defers loading)
2. **importlib** - `from importlib import import_module` (programmatic)
3. **PEP 810** - `lazy import datetime` (future feature)

### Trade-offs

Lazy loading improves startup time but makes dependency visualization harder.

## Key Takeaways

- **All import problems trace back to `sys.path`**
- Python doesn't auto-discover code - you must direct it via imports
- Search stops at first match (can cause shadowing)
- Modules are singletons (cached in `sys.modules`)
- Running as script vs module changes `sys.path` behavior
- Use absolute imports when possible
- Understand `__init__.py` purpose in packages