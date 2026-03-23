# Import is Important Tutorial
## Warm Up Exercises

### Learning Objectives
By the end of this lab, you will be able to:

1. Write correct `import` statements using both absolute and relative import syntax
1. Refactor code into separate modules while maintaining proper import relationships between files
1. Organize Python code using packages with `__init__.py` files
1. Use `__init__.py` files to control package initialization and automatic imports
1. Apply relative imports within package hierarchies
1. Diagnose and resolve common import errors including `NameError`, `ImportError`, `AttributeError`, and `ModuleNotFoundError`

### Setup Instructions

1. Follow these [setup instructions](./lab_spec/setup.md), then return here to get started
1. Use the integrated terminal to navigate to the `import-warmup/` directory if you're not already there
1. Verify that your Codespace is set up correctly by running `python3.14 --version`. The output should be `Python 3.14.0`.

### Exercise 1: Basic Imports

This exercise introduces the types of errors you'll see when your imports are missing or incorrect, as well as providing practice on fixing them.

#### Task 1.1: Correct Initial `import` Errors

Run the `run_exercises.py` file:

```bash
python3.14 run_exercises.py
```

You'll see the following `NameError`:

```code
File "/workspaces/import-warmup/run_exercises.py", line 1, in <module>
    my_portfolio = portfolio.data.create_portfolio("Retirement")
                   ^^^^^^^^^
NameError: name 'portfolio' is not defined
```

Add `import` statement(s) to the `run_exercises.py` file so that the above `NameError` is resolved. Do not change any other code in the file.

##### Success

If you've succeeded, the `NameError: name 'portfolio' is not defined` error is replaced with a new error: `NameError: name 'make_asset' is not defined`

##### Reflection
1. What's the difference between a `NameError` and an `ImportError` in the context of imports?
2. Why does Python require explicit import statements rather than automatically finding all available code?

#### Task 1.2: Correct `NameError`

The error message tells you that `make_asset` is not defined. Find where `make_asset` is defined and add the necessary import statement(s) to the file(s) that use it. Do not modify any of the existing code.

##### Success

You'll know you succeeded when the above `NameError` is replaced with the following error:

```code
Traceback (most recent call last):
  File "/workspaces/import-warmup/run_exercises.py", line 4, in <module>
    portfolio.report.print_report(my_portfolio)
    ^^^^^^^^^^^^^^^^
AttributeError: module 'portfolio' has no attribute 'report'
```

**Note:** You may have thought ahead during Task 1.1, above, and may have already corrected the problem that causes the `AttributeError` above. If you don't see the above `AttributeError`, get no other errors and your report prints to the screen, follow the link at the end of this document to go to Part 2 of the lab.

#### Task 1.3: Correct further errors revealed in `run_exercises.py`

Add `import` statement(s) to `run_exercises.py` so that the above `AttributeError` is resolved. Do not modify any of the existing code.

##### Success

You'll know you succeeded when running `python3.14 run_exercises.py` results in no errors and you have a report printed to the screen.

#### Task 1.3: Commit and Push your Changes

Run `git status` on your repo to see the changes you made. You'll notice that there are several `__pycache__` folders in your codebase. These are auto-generated when you import modules into your code and contain bytecode for the modules you import in your project as a way of speeding up subsequent imports. They can be safely deleted since they'll be regenerated when needed, so they should not be committed to your repo.

Create a `.gitignore` file in your repo and add `__pycache__` to it. Add, commit, and push your changes to your repo.

---

Next up: Exercise 2: [Imports and Refactored Code](./lab_spec/02_Exercise2.md)


