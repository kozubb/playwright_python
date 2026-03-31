# Playwright with Python - E2E Testing

## Project Description

This project demonstrates an end-to-end (E2E) testing framework using **Playwright** with **Python**. It includes automated tests for:

---

## Key Features

### Frontend Tests

1. **QA Brains**
   - Existing frontend tests for the QA Brains website.
   - Includes login, registration, and product purchase flows.
   - Implemented using **Page Object Pattern** for maintainability and clarity.

## Test Strategy

The project follows a balanced testing pyramid approach.

### Frontend E2E Tests

- Focus only on business-critical user flows
- Validate real UI behavior from an end-user perspective
- Avoid over-testing UI details
- Written with stability and readability in mind

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
