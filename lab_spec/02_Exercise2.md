# Import is Important Tutorial
## Warm Up Exercises

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
1. `run_exercises.py` runs without errors and prints the portfolio report.

Add, commit, and push your changes to your repo.

##### Reflection
1. Why is it a good idea to move repeated code into modules?
1. What would happen if the module got moved into another subfolder? How would you correct these errors?

---

Next up: [Exercise 3: Packages and Relative Imports](03_Exercise3.md)