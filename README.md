# Python Port Scanner

A simple TCP port scanner built with Python using the python-nmap library.

## Features
- Scan multiple ports on a target host
- Detect open, closed, and filtered ports
- Command-line interface for easy usage

## Technologies Used
- Python
- Nmap
- Kali Linux
- Git

## Installation

Install dependencies:

pip install python-nmap

## Usage

python3 port_scanner.py -o <host> -p <ports>

Example:

python3 port_scanner.py -o scanme.nmap.org -p 80,443

## Author

MP0701
