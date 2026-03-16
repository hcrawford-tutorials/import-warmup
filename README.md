# Import is Important Tutorial
## Warm Up Exercises

### Learning Objectives
By the end of this lab, you will be able to:

1. Write correct `import` statements using both absolute and relative import syntax
1. Refactor code into separate modules while maintaining proper import relationships between files
1. Organize Python code using packages with __init__.py files
1. Use __init__.py files to control package initialization and automatic imports
1. Apply relative imports within package hierarchies
1. Diagnose and resolve common import errors including `NameError`, `AttributeError`, and `ModuleNotFoundError`

### Setup Instructions

1. Follow these [setup instructions](./setup.md), then return here to get started
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
File "/workspaces/import-warmup/run-exercises.py", line 1, in <module>
    my_portfolio = portfolio.data.create_portfolio("Retirement")
                   ^^^^^^^^^
NameError: name 'portfolio' is not defined
```

Add `import` statement(s) to the `run-exercises.py` file so that the above `NameError` is resolved. Do not change any other code in the file.

##### Success

If you've succeeded, the `NameError: name 'portfolio' is not defined` error is replaced with a new error: `NameError: name 'make_asset' is not defined`

##### Reflection
1. What's the difference between a `NameError` and an `AttributeError` in the context of imports?
2. Why does Python require explicit import statements rather than automatically finding all available code?

#### Task 1.2: Correct `NameError`

The error message tells you that `make_asset` is not defined. Find where `make_asset` is defined and add the necessary import statement(s) to the file(s) that use it. Do not modify any of the existing code.

##### Success

You'll know you succeeded when the above `NameError` is replaced with the following error:

```code
Traceback (most recent call last):
  File "/workspaces/import-warmup/run-exercises.py", line 4, in <module>
    portfolio.report.print_report(my_portfolio)
    ^^^^^^^^^^^^^^^^
AttributeError: module 'portfolio' has no attribute 'report'
```

#### Task 1.3: Correct further errors revealed in `run-exercises.py`

Add `import` statement(s) to `run-exercises.py` so that the above `AttributeError` is resolved. Do not modify any of the existing code.

##### Success

You'll know you succeeded when running `python3.14 run_exercises.py` results in no errors and you have a report printed to the screen.

### Exercise 2: Imports and Refactored Code

In this exercise, you'll see how refactoring code can break existing `import` statements, and how to refactor `import` statements to suit the changes.

#### Task 2.1: Refactoring and Namespaces
Review the code in `portfolio/assets.py` and `portfolio/report.py`. Notice the following:

- The `calculate_asset_value()` and `calculate_portfolio_value()` functions are found in both files.
- A recent code review suggested that neither function belongs in `portfolio/assets.py` because they act upon an asset rather than being part of an asset. They also don't belong in `portfolio/report.py` because they're not about a report, either.

Create a new module called `portfolio/metrics.py`. Refactor the two functions into this file and import them back into the original file(s). Do not change any other code in the original file(s) (i.e., make the `import` statements work with the existing code rather than changing the existing code to make your `import` statements work.)

##### Success:

You'll know you succeeded if:
1. The `calculate_asset_value()` and `calculate_portfolio_value()` functions appear only in `metrics.py`
1. `run-exercises.py` runs without errors and prints the portfolio report.

##### Reflection
1. Why is it a good idea to move repeated code into modules?
1. What would happen if the module got moved into another subfolder? How would you correct these errors?

### Exercise 3: Packages and Relative Imports
Our code is looking good, but having all of the modules lumped into the `portfolio` folder makes it hard to understand how each module is linked to the others. Packages are one way to provide organization to your codebase, but the imports you use change when this structure changes.

This exercise will give you practice with using `import` statements within packages, specifically with using relative imports.

#### Task 3.1: Add a package to your current project
Within the `portfolio/` directory, add a subdirectory called `core/`. Add an empty `__init__.py` file to `core/`.

#### Task 3.2: Move in some files
Move `assets.py` and `metrics.py` into `core/`. Your directory structure should look like this when you're finished:

```
portfolio/
├── core/
│   ├── __init__.py
│   ├── assets.py
│   └── metrics.py
├── data.py
└── report.py
```

At this point, executing `run-exercises.py` will result in a `ModuleNotFoundError`.

##### Reflection
1. Is `core/` a regular package or a namespace package? Does it matter which one it is? Why or why not? What benefits does one type have over the other?

#### Background: Relative vs Absolute Imports
When working with packages, you can import using:
- **Absolute imports**: specify the entire package structure in the import statement. They're generally preferred because they're unambiguous.
- **Relative imports**: use dots (`.`) to indicate the current package 
level. They're sometimes used within packages because they remain valid 
if the package is renamed.

#### Task 3.3: Update Imports

Update your imports in all files so that all errors are resolved, and the report prints as expected. Use relative imports rather than absolute imports wherever possible (i.e., whenever a file containing an `import` statement is in a subpackage).

##### Success
You'll know you succeeded when the report prints as expected, with no errors thrown.

#### Task 3.4: "Automatic" Imports
While the program runs as expected, it seems strange to have to explicitly import `report.py` and `data.py` into the main program since we'll likely always want to print a report, and we'd need a portfolio created first. Instead, the relevant files should be always imported when importing the enclosing package, without explicitly stating it in every file. This is a job for `__init__.py`!

Modify the project so that you no longer have to explicitly import the `report.py` and `data.py` files into `run-exercises.py`.

##### Success

You'll know you succeeded when:
1. `report` and `data` are no longer explicitly imported into `run-exercises.py`
1. The report prints as expected

##### Reflection
1. What are the trade-offs of using `__init__.py` for automatic imports versus requiring explicit imports in every file?
2. When might automatic imports be problematic? (Consider: circular dependencies, namespace pollution, import performance)
