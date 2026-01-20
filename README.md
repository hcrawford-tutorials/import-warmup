# Import is Important Tutorial
## Warm Up Exercises

These exercises allow you to practice to concepts needed to understand import statements. You'll use the resources in the `import-warmup/portfolio` folder for these exercises.

### Exercise 1: Basic Imports

This exercise introduces the types of errors you'll see when your imports are missing or incorrect, as well as providing practice on fixing them.

#### Step 1

Make sure you're in the root folder, which is called `import-warmup`. Run the `run-exercises.py` file:

```python
python3.14 run_exercises.py
```

You'll see the following `NameError`:

```code
File "/workspaces/import-warmup/run-exercises.py", line 1, in <module>
    my_portfolio = portfolio.data.create_portfolio("Retirement")
                   ^^^^^^^^^
NameError: name 'portfolio' is not defined
```

#### Step 2

Add `import` statement(s) to the `run-exercises.py` file so that the above `NameError` is resolved. Do not change any other code in the file.

##### Success

If you've succeeded, the `NameError: name 'portfolio' is not defined` error is replaced with a new error: `NameError: name 'make_asset' is not defined`

#### Step 3

Add `import` statement(s) to the relevant files so that the above `NameError` is resolved. Do not modify any of the existing code.

##### Success

You'll know you succeeded when the above `NameError` is replaced with the following error:

```code
Traceback (most recent call last):
  File "/workspaces/import-warmup/run-exercises.py", line 4, in <module>
    portfolio.report.print_report(my_portfolio)
    ^^^^^^^^^^^^^^^^
AttributeError: module 'portfolio' has no attribute 'report'
```

#### Step 4: Further errors revealed in `run-exercises.py`

Add `import` statement(s) to `run-exercises.py` so that the above `AttributeError` is resolved. Do not modify any of the existing code.

##### Success

You'll know you succeeded when running `python3.14 run-exercises.py` results in no errors and you have a report printed to the screen.

### Exercise 2: Imports and Refactored Code

In this exercise, you'll see how refactoring code can break our imports, and how import statements must be refactored to suit the changes.

#### Step 1
Review the code in `portfolio/assets.py`. A recent code review suggested that `calculate_asset_value()` and `calculate_portfolio_value()` does not belong in `portfolio/assets.py` because it acts upon an asset rather than being part of an asset. It also doesn't belong in `portfolio/report.py` because it's not about a report, either.

Create a new module called `portfolio/metrics.py`. Refactor the two functions into this file and import them back into the original file(s). Do not change any other code in the original file(s) (i.e., make the `import` statements work with the existing code rather than changing the existing code to make your `import` statements work.)

##### Success:

You'll know you succeeded if:
1. The `calculate_asset_value()` and `calculate_portfolio_value()` functions appear only in `metrics.py`
1. `portfolio/run-exercises.py` runs without errors and prints the portfolio report.

##### Reflection
1. Why is it a good idea to move repeated code into modules?
1. What would happen if the module got moved into another subfolder? How would you correct these errors?

### Exercise 3: Packages and Collisions

This exercise will give you practice with using import statements within packages, specifically with using relative imports, as well as the errors that can happen with name collisions and how to resolve them.

#### Step 1: Add a package to your current project
Within the `portfolio/` directory, add a subdirectory called `core/`, and add an `__init__.py` file to `core/`.

#### Step 2: Move in some files
Move `assets.py` and `metrics.py` into `core/`. Your directory structure should look like this when you're finished:

TODO ADD IMAGE

At this point, executing `run-exercises.py` will result in a `ModuleNotFoundError`.

##### Reflection
1. Is `core/` a regular package or a namespace package? Does it matter which one it is? Why or why not? What benefits does one type have over the other?

#### Step 3: Update Imports

Update your imports in all files so that all errors are resolved, and the report prints as expected. Use relative imports rather than absolute imports wherever possible (i.e., whenever a file containing an `import` statement is in a subpackage).

##### Success
You'll know you succeeded when the report prints as expected, with no errors thrown.

#### Step 4: "Automatic" Imports
While the program runs as expected, it seems strange to have to explicitly import `report.py` and `data.py` into the main program since we'll likely always want to print a report, and we'd need a portfolio created first. Instead, the relevant files should be always imported when importing the enclosing package, without explicitly stating it in every file. This is a job for `__init__.py`!

Modify the project so that you no longer have to explicitly import `report.py` and `data.py` into `run-exercises.py`.

##### Success

You'll know you succeeded when:
1. `report` and `data` are no longer explicitly imported into `run-exercises.py`
1. The report prints as expected


TODO: Add some Reflection questions to each part. Get people thinking about tradeoffs.