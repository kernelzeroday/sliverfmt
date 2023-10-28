import sys
import argparse

def process_input(input_stream, command):
    for line in input_stream:
        parts = line.strip().split(' ')
        if parts:
            uuid = parts[0]
            formatted_command = f"use {uuid}\n{command}"
            print(formatted_command)

def main():
    parser = argparse.ArgumentParser(description="Process UUIDs and apply a command.")
    parser.add_argument("command", help="The command to apply to the UUIDs.")
    args = parser.parse_args()

    process_input(sys.stdin, args.command)

if __name__ == "__main__":
    main()

