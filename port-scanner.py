import socket
import asyncio
import logging
import argparse

logging.basicConfig(filename='port_scanner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

welcome_banner = """
______          _     _____                                 
| ___ \        | |   /  ___|                                
| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                            

Created By :- Wathsala Dewmina

"""
print(welcome_banner)

async def scan_port(ip, port, timeout):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout)
        writer.close()
        await writer.wait_closed()
        return port, True
    except Exception:
        return port, False

async def run_scanner(ip, ports, timeout):
    open_ports = []
    tasks = [scan_port(ip, port, timeout) for port in ports]
    for task in asyncio.as_completed(tasks):
        port, is_open = await task
        if is_open:
            open_ports.append(port)
            logging.info(f'Port {port} is open.')
            print(f'Port {port} is open.')
    return open_ports

async def banner_grabbing(ip, port, timeout):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.write(b'Hello\r\n')
        await writer.drain()
        banner = await reader.read(1024)
        writer.close()
        await writer.wait_closed()
        return banner.decode().strip()
    except Exception:
        return 'No banner'

async def main(target, start_port, end_port, timeout):
    ports = range(start_port, end_port + 1)
    open_ports = await run_scanner(target, ports, timeout)

    for port in open_ports:
        banner = await banner_grabbing(target, port, timeout)
        logging.info(f'Port {port} - Banner: {banner}')
        print(f'Port {port} - Banner: {banner}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advanced Python Port Scanner')
    parser.add_argument('target', type=str, help='Target IP address')
    parser.add_argument('start_port', type=int, help='Start port number')
    parser.add_argument('end_port', type=int, help='End port number')
    parser.add_argument('--timeout', type=float, default=1.0, help='Timeout for port scan (default: 1.0 seconds)')
    args = parser.parse_args()

    asyncio.run(main(args.target, args.start_port, args.end_port, args.timeout))
