# Mega-Million-lottery-ticket-generator

This GitHub repository contains a Python script that simulates the process of generating Mega Millions lottery tickets. Users can specify the number of tickets they want to generate, and the script will produce random, non-repeating sets of numbers for each ticket, along with a Mega Ball number.

## Features

- **Customizable Ticket Generation**: Allows users to specify the number of Mega Millions tickets they wish to generate.
- **Random Number Selection**: Each ticket includes five unique random numbers (from 1 to 75) and one Mega Ball number (from 1 to 25).
- **Sorted Numbers**: The five numbers on each ticket are sorted in ascending order for ease of reading.
- **Tabulated Display**: Tickets are displayed in a clear, tabulated format, making it easy to read and understand the output.

## Usage

1. **Run the Script**: Execute the Python script in your preferred environment.
2. **Input Request**: The script will prompt the user to enter the desired number of tickets.
3. **Ticket Display**: Once the number of tickets is entered, the script generates the tickets and displays them in a tabulated format.

## Example

```python
How many tickets would you like? 3

My 3 Mega Millions ticket:

  Ticket    Ball 1    Ball 2    Ball 3    Ball 4    Ball 5    Mega Ball
--------  --------  --------  --------  --------  --------  -----------
       1        12        23        34        45        59            22
       2         5        17        28        39        48            14
       3         8        19        27        36        51            9
```

## Requirements

- Python 3.x
- `tabulate` Python package for formatted output

## Installation

Ensure that Python 3.x is installed on your system. If not, it can be downloaded and installed from [python.org](https://www.python.org/).

The `tabulate` package is required for displaying the tickets. It can be installed using pip:

```bash
pip install tabulate
```
