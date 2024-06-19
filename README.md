# Urban Routes Automation Testing with Selenium

This repository contains an automation testing project using Selenium and Python for a transportation service similar to Uber. The tests are designed to automate the process of requesting a taxi, selecting a tariff, entering client information, making a payment, and requesting for additional perks. 

## Project Overview
This project automates key functionalities of a web-based taxi service application. The automation scripts are written in Python, leveraging the Selenium WebDriver to interact with the web elements. The goal is to ensure that the main features of the application work as expected, providing a smooth user experience.

## Features Tested
1. **Setting the Route**: Automates the input of start and end addresses.
2. **Requesting a Taxi**: Simulates the process of asking for a taxi.
3. **Selecting a Tariff**: Tests the selection of different tariffs, including the "Comfort" option.
4. **Entering Phone Number**: Automates entering the phone number and confirming it with a code.
5. **Adding Payment Method**: Adds a credit card and verifies the payment method.
6. **Commenting to Driver**: Allows users to send a comment to the driver.
7. **Making Special Requests**: Includes options for requesting a blanket or ice cream.
8. **Calling for a Taxi**: Completes the process by confirming the taxi request.

## Project Structure
1. **main.py**: The entry point for running the automated tests sequentially.
2. **requesting_taxi.py**: Contains the core classes and methods for the automation scripts.
  - `UrbanRoutesPages`: Defines the web elements and their locators.
  - `TestUrbanRoutes`: Implements the setup, tests, and teardown methods.
3. **data.py**: Stores the test data such as URLs, addresses, phone numbers, and card details.

## Getting Started
### Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver (or your browser of preference)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/urban-routes-automation.git
   cd urban-routes-automation
   ```
2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Tests
1. Ensure you have ChromeDriver installed and it's in your PATH.
2. Run the main script:
   ```sh
   python main.py
   ```

### Project Files
- **main.py**: Manages the execution flow of the test cases.
- **requesting_taxi.py**: Contains the classes and methods for interacting with the web application.
- **data.py**: Holds the test data and configuration.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

