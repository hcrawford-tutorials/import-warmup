# Import is Important Tutorial
## Warm Up Exercises

### Exercise 3: Packages and Relative Imports
Our code is looking good, but having all of the modules lumped into the `portfolio` folder makes it hard to understand how each module is linked to the others. Packages are one way to provide organization to your codebase, but the imports you use change when this structure changes.

This exercise will give you practice with using `import` statements within packages, specifically with using relative imports.

#### Task 3.1: Add a package to your current project
Within the `portfolio/` directory, add a subdirectory called `core/`. Add an empty `__init__.py` file to `core/`. 

#### Task 3.2: Move in some files
Move `assets.py` and `metrics.py` into `core/`. If you're prompted to accept refactoring changes, choose `Skip Changes`. The refactors are what you'll do in this lab!

Your directory structure should look like this when you're finished:

```
portfolio/
├── core/
│   ├── __init__.py
│   ├── assets.py
│   └── metrics.py
├── data.py
└── report.py
```

At this point, executing `run_exercises.py` will result in a `ModuleNotFoundError`.

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

Modify the project so that you no longer have to explicitly import the `report.py` and `data.py` files into `run_exercises.py`.

##### Success

You'll know you succeeded when:
1. `report` and `data` are no longer explicitly imported into `run_exercises.py`
1. The report prints as expected

##### Reflection
1. What are the trade-offs of using `__init__.py` for automatic imports versus requiring explicit imports in every file?
2. When might automatic imports be problematic? (Consider: circular dependencies, namespace pollution, import performance)

---

Congrats! You've finished the warm up exercises!