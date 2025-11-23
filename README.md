# Python Banking System

## Introduction

This Python program is a simple interactive banking system designed to simulate basic bank account operations in a command-line environment. It allows a user to:

- Open a new bank account with an initial deposit.
- Deposit money.
- Withdraw money (with balance validation).
- Check the current balance.
- View a detailed transaction history for transparency.
- Exit the system cleanly.

This project serves as an excellent foundation for learners to grasp fundamental programming concepts such as input validation, loops, exception handling, and transaction management in Python.

## Key Features

- **Account Initialization:** Opens an account by requiring a positive initial deposit, preventing invalid attempts.
- **Menu-driven Interface:** Displays clear options to navigate through banking operations.
- **Deposits and Withdrawals:** Validates inputs, updates balance accordingly, and ensures withdrawals don't exceed available funds.
- **Balance Inquiry:** Provides the current account balance on demand.
- **Transaction History:** Records each deposit, withdrawal, and opening deposit, displaying them on request.
- **Robust Error Handling:** Gracefully catches non-numeric inputs and invalid values, prompting users with helpful feedback.
- **In-memory Session Data:** Maintains data only during the session, simplifying the program while covering core functionality.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system. Download from [python.org](https://www.python.org/downloads/).

### Downloading the Code

- Download or clone the repository.
- Copy the full banking system code into a file named `bank_system.py`.

### Running the Program

1. Open your terminal or command-line interface.
2. Navigate to the folder containing `bank_system.py`.
3. Run the program using:4. Follow the on-screen prompts to interact with the banking system.

## Usage Guide

- When prompted, enter a positive numeric value to open your bank account.
- Use the menu options:

1. **Deposit Money:** Enter an amount greater than zero to add funds.
2. **Withdraw Money:** Enter an amount to withdraw, which must be positive and within your current balance.
3. **Check Balance:** Displays your current available balance.
4. **Transaction History:** Shows all your transactions for the session.
5. **Exit:** Close the program.

- Invalid inputs or menu selections prompt clear error messages to guide correct usage.

## Code Overview

### Account Opening Logic
- Utilizes a `while True` loop and `try-except` block to ensure a valid positive initial deposit is entered before proceeding.
- Sets the initial balance and records the deposit in the transaction history.

### Main Banking Menu
- Repeatedly presents a five-choice menu for deposits, withdrawals, balance check, transaction history, and exit.
- Each choice invokes appropriate logic with input validation and updates the balance and transaction history accordingly.

### Input Validation and Error Handling
- Implements `try-except` blocks around all numeric inputs to catch non-numeric entries.
- Checks conditions such as positivity of amounts and sufficient funds for withdrawals.
- Provides friendly, descriptive error messages to enhance user experience.

### Data Management
- Uses a floating-point variable `balance` to track funds.
- Stores transaction records as strings in a list `history`.
- Data exists only for the current runtime session (no persistence).

## Future Enhancements

- **Object-Oriented Design:** Refactor using classes to encapsulate account behaviors.
- **Data Persistence:** Save/load account details and transaction logs to/from files or databases.
- **Multi-Account Support:** Enable management of multiple accounts with authentication.
- **Graphical or Web Interface:** Upgrade user interaction through GUIs or web applications.
- **Additional Features:** Add functions like funds transfer, interest calculations, loan management, and account types.
- **Security and Logging:** Introduce authentication, encryption, and transaction audit logs.

---

Thank you for using the Python Banking System! Contributions and feedback are welcome.


