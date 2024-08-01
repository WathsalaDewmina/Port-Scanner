# Python Port Scanner

This is a simple Python port scanner script that allows you to scan a target IP address or hostname for open ports within a specified range.

## Features

- Scans a target IP or hostname for open ports.
- Allows setting a timeout for each port scan attempt.

## Requirements

- Python 3.x

## Installation

To get started with the port scanner, you'll need to install the required dependencies. You can do this using `pip`.

```bash
pip install -r requirements.txt

## Usage

To run the port scanner, use the following command:

```bash
python port-scanner.py [-h] [--timeout TIMEOUT] target start_port end_port
```

### Arguments

- `target`: The target IP address or hostname to scan.
- `start_port`: The starting port number of the range to scan.
- `end_port`: The ending port number of the range to scan.

### Optional Arguments

- `-h`, `--help`: Show the help message and exit.
- `--timeout TIMEOUT`: Set a timeout for each port scan attempt (default is 1 second).

### Example

```bash
python port-scanner.py 192.168.1.1 20 80
```

This command will scan the target IP `192.168.1.1` for open ports in the range 20-80.

```bash
python port-scanner.py --timeout 2 example.com 1 1024
```

This command will scan the target `example.com` for open ports in the range 1-1024 with a timeout of 2 seconds per port scan attempt.

## License

This project is licensed under the MIT License.
```
