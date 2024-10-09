# Movie Ticket Availability Checker

This project is a **Python script** that uses **Selenium** to check for movie ticket availability on a website and notifies the user via email when tickets become available. The script logs the activity and errors, and includes optional features such as displaying a "Get Tickets" button when tickets are found.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logging](#logging)

## Features
- Automated movie ticket availability checks using Selenium.
- Email notifications when tickets are available.
- Logging of script activity and errors.
- Uses `.env` file to store sensitive information like email credentials.

## Technologies
- **Python** (v3.10)+
- **Selenium** for web automation
- **smtplib** for sending emails
- **Logging** for recording script activity
- **ChromeDriver** for interacting with the Chrome browser

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yousufmohi/ticket_checker.git
    cd ticket_checker
    ```

2. Install the required dependencies:

    ```bash
    pip install selenium chromedriver-autoinstaller
    ```

3. Download the appropriate **ChromeDriver** for your Chrome browser version, or use the **chromedriver-autoinstaller** package to automatically install it:

    ```python
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()
    ```

## Usage
1. Make sure you have configured your `.env` file with your email credentials and other necessary information (see [Configuration](#configuration)).

2. Run the script:

    ```bash
    python src\main.py
    ```

3. The script will:
   - Continuously check for ticket availability.
   - Send an email notification if tickets are available.
   - Log activity to a file in the `logs/` directory.

## Configuration
Create a `.env` file in the root of the project to store sensitive information:

- Replace the placeholders with actual values.
- Keep this file secret and add it to your `.gitignore` file to prevent it from being pushed to version control.

## Logging
The script logs its activity and errors to a `logs/` folder. Ensure that this directory exists.



