#!/usr/bin/python3

""" code """

import sys
import signal

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Print the collected statistics."""
    global total_size, status_codes
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption signal."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Strip the line of leading/trailing whitespace
        line = line.strip()
        
        # Split the line by spaces to parse the components
        parts = line.split()
        
        # Check if the line format is correct
        if len(parts) != 7:
            continue
        
        ip_address, dash, date, request, http_version, status_code, file_size = parts
        
        # Validate and parse status code and file size
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue
        
        # Update total file size
        total_size += file_size
        
        # Update the status code count if it's one of the expected ones
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        # Increment the line count
        line_count += 1
        
        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    # In case of an unexpected exception, print the statistics before exiting
    print(f"An error occurred: {e}")
    print_statistics()
    sys.exit(1)
