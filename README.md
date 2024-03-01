
# Python Environment Setup and Script Execution Guide

This guide provides step-by-step instructions on how to set up your Python environment and run a script designed to analyze phone numbers from Excel files. The script merges data from multiple Excel files, identifies the most repeated phone numbers, and flags numbers that are excessively repeated.

## Prerequisites

Before you begin, ensure you have the following:
- Python installed on your computer. This guide assumes you are using Python 3.6 or higher.
- A `requirements.txt` file that lists all the necessary Python packages for running the script.

## Step 1: Installing Python

If you haven't already installed Python, follow these steps:
1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the latest version of Python for your operating system.
3. Run the installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" during installation.

## Step 2: Setting Up Your Python Environment

1. Open a terminal or command prompt on your computer.
2. Navigate to the folder where you want to store your script and Excel files.
3. Create a virtual environment by running:
   ```bash
   python -m venv myenv
   ```
   Replace `myenv` with your preferred name for the virtual environment.

4. Activate the virtual environment:
   - On Windows, run:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```bash
     source myenv/bin/activate
     ```

5. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Preparing Your Excel Files

1. Create a folder named `data` in the same directory as your Python script.
2. Place all your Excel files (.xlsx format) that you want to analyze into the `data` folder. Ensure that each Excel file has one or more columns starting with "PHONE NUMBER".

## Step 4: Running the Script

1. Ensure your virtual environment is activated and you are in the directory containing the script.
2. Run the script by executing:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your Python script.

The script will read all Excel files in the `data` folder, merge them, analyze the phone numbers, and print the results in the terminal. It will display the top 25 most repeated phone numbers, format counts with thousands separators, and alert if any phone numbers are repeated more than 50 times.

## Additional Notes and Example

- Phone numbers should ideally be unique or repeated no more than 3 or 4 times to ensure data integrity and privacy.
- If you encounter any issues with the script or have suggestions for improvement, consider reviewing the code for potential updates or reaching out for support.

![CleanShot 2024-03-01 at 18 43 25@2x](https://github.com/ignacioaraya1995/PhoneReview/assets/21697653/be6964e8-57a3-43fe-a61c-25c516a1bf13)


Happy analyzing!
