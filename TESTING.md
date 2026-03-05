# Testing Strategy — Quick-Calc

## Overview

This document describes the testing strategy applied to the Quick-Calc project, explains the rationale behind what was and was not tested, and connects the approach to the core concepts covered in Lecture 3 (Software Engineering & Testing).

## What Was Tested

The test suite covers two layers:

- **Core arithmetic functions** (`add`, `subtract`, `multiply`, `divide`) — tested in isolation through unit tests to confirm correct output for standard inputs and edge cases.
- **Calculator workflow** — tested through integration tests that simulate real user interactions (entering numbers, selecting operators, pressing equals, and clearing state).

Edge cases were specifically targeted: division by zero, negative numbers, decimal inputs, very large numbers, and operations that produce negative results.

## What Was Not Tested

- **User interface / CLI input parsing:** The `main()` function handles raw string input from the terminal. Testing it would require mocking `input()` and `print()`, which adds complexity without meaningfully validating calculation correctness. This falls under system-level testing and was considered out of scope for this assignment.
- **Non-functional attributes:** Performance benchmarks, security, and usability were not tested. The application is a simple calculator with no network, database, or concurrency requirements.

## Lecture Concepts

### 1. The Testing Pyramid

The Testing Pyramid recommends having many unit tests at the base, fewer integration tests in the middle, and very few end-to-end or UI tests at the top. This project follows that structure: 10 unit tests form the broad foundation, verifying each pure function independently. Above that, 3 integration tests check that the `Calculator` class correctly coordinates the pure functions through realistic workflows. No end-to-end UI tests were written, keeping the pyramid shape intact. This distribution means most feedback comes from fast, isolated unit tests, while integration tests catch wiring issues between components.

### 2. Black-Box vs White-Box Testing

The unit tests primarily use a **black-box** approach — they call each function with specific inputs and assert expected outputs without relying on knowledge of internal implementation. For example, `test_divide_by_zero_raises_error` only checks that a `ValueError` is raised; it does not inspect how the guard clause is written. The integration tests also follow a black-box style: they simulate the sequence of actions a user would perform (enter number → set operator → enter number → equals) and verify the final displayed result without examining internal state transitions. This makes the tests resilient to refactoring — if the implementation changes but behaviour stays the same, no tests need updating.

### 3. Functional vs Non-Functional Testing

All tests in this project are **functional tests** — they verify that the software produces correct outputs for given inputs, which is the core requirement for a calculator. **Non-functional testing** (performance, load, security, usability) was intentionally excluded. A simple CLI calculator has no meaningful performance thresholds to measure, no user authentication, and no concurrent access. In a larger project, non-functional tests would be added to verify response times under load or accessibility compliance, but for Quick-Calc the functional layer provides sufficient quality assurance.

### 4. Regression Testing

The test suite is structured to serve as a **regression safety net**. If a future developer modifies the division logic or changes how the `Calculator` class chains operations, running `pytest` will immediately flag any broken behaviour. Because the tests use clear, descriptive names and cover both standard cases and edge cases, a failing test pinpoints exactly which operation or scenario regressed. In a CI/CD pipeline, this suite would run automatically on every commit, preventing regressions from reaching production.

## Test Results Summary

| # | Test Name | Type | Status |
|---|-----------|------|--------|
| 1 | `test_add_positive_numbers` | Unit | ✅ Pass |
| 2 | `test_subtract_positive_numbers` | Unit | ✅ Pass |
| 3 | `test_multiply_positive_numbers` | Unit | ✅ Pass |
| 4 | `test_divide_positive_numbers` | Unit | ✅ Pass |
| 5 | `test_divide_by_zero_raises_error` | Unit | ✅ Pass |
| 6 | `test_add_negative_numbers` | Unit | ✅ Pass |
| 7 | `test_multiply_by_zero` | Unit | ✅ Pass |
| 8 | `test_divide_decimal_numbers` | Unit | ✅ Pass |
| 9 | `test_subtract_resulting_negative` | Unit | ✅ Pass |
| 10 | `test_multiply_large_numbers` | Unit | ✅ Pass |
| 11 | `test_full_addition_workflow` | Integration | ✅ Pass |
| 12 | `test_clear_resets_after_calculation` | Integration | ✅ Pass |
| 13 | `test_chained_operations` | Integration | ✅ Pass |
