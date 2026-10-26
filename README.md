# Bug Fixing Using Cursor AI (Assignment 8)

Application of Test-Driven Debugging (**Red -> Fix -> Green**) and AI-assisted root cause analysis in **Cursor AI**.

## Overview
This project showcases identifying, isolating, and fixing bugs in a grade calculation engine using Python's standard `unittest` framework and Cursor AI debugging workflows.

## TDD Debugging Methodology
* **RED:** Wrote and executed 9 unit tests exposing boundary failures and logic defects in the uncorrected program.
* **FIX:** Leveraged targeted AI prompts to isolate the exact failing line or condition without prematurely rewriting the codebase.
* **GREEN:** Implemented targeted fixes and verified that all 9 unit tests run and pass cleanly.

## Bug Observation Table
| Bug Area | Cause | Fix Applied |
| :--- | :--- | :--- |
| **Average Calculation** | Truncating division and unhandled empty score list exception | Added empty check fallback and floating-point mean calculation via `sum(scores) / len(scores)` |
| **Passing Boundary** | Used strict inequality (`> 40`) failing students scoring exactly on boundary | Changed condition to inclusive inequality (`>= 40`) |
| **Grade Ordering** | Inverted condition precedence assigning incorrect lower tiers to high performers | Restructured conditional cascade in strict descending threshold order (`>= 90`, `>= 80`, etc.) |

## Test Verification
Run the unit test suite:
```bash
python test_grade_calculator.py
```
Output:
```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## Technologies Used
* **Python 3.x**
* **unittest**
* **Cursor AI Debugging**

## Author
* **Name:** Sakshi Sharma (B.Tech CSE, 2nd Year)
* **University:** JECRC University
