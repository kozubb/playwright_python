# Playwright with Python - E2E Testing

## Project Description

This project demonstrates an end-to-end (E2E) testing framework using **Playwright** with **Python**. It includes automated tests for:

- **Frontend testing**: login, registration, and product purchase process.
- **API testing**: testing GET, POST, PUT, and DELETE requests.
- **CI/CD pipeline**: integrated fully with **GitHub Actions**, including test execution and reporting.

---

## Key Features

### Frontend Tests

1. **QA Brains**
   - Existing frontend tests for the QA Brains website.
   - Includes login, registration, and product purchase flows.
   - Implemented using **Page Object Pattern** for maintainability and clarity.

### API Tests

- GET, POST, PUT, and DELETE requests

### CI/CD with GitHub Actions

- **Automated Workflow**: Full integration of Playwright tests triggered on every push and manually on demand.
  - **Direct Summary**: Test results are visible directly in the GitHub Actions summary for quick feedback.

### Test Documentation

- Detailed comments in the test code for easy understanding of the test flow, especially for non-technical people.

## Test Strategy

The project follows a balanced testing pyramid approach.

### Frontend E2E Tests

- Focus only on business-critical user flows
- Validate real UI behavior from an end-user perspective
- Avoid over-testing UI details
- Written with stability and readability in mind

### API Tests

- Faster and more reliable than UI tests
- Used to validate backend logic independently
- Reduce the need for excessive E2E coverage

---

## Design Decisions

### Page Object Pattern

- Each page has its own class containing:
  - UI actions
  - Validations
  
- **Benefits:**
  - Tests remain clean and focused only on business flow
  - Easier maintenance when selectors or UI structure change

### Chrome-only Execution

- Chrome is selected as the primary browser because:
  - It reflects the most common real-user environment
  - Reduces test flakiness
  - Simplifies CI configuration
