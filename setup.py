import os
import subprocess
import time


def open_terminal_in_dir_with_command(directory, command):
    """Opens a new Windows Terminal tab, navigates to the directory, and runs a command."""
    subprocess.Popen(['wt.exe', '-w', '0', 'nt', '-d',
                     directory, 'bash', '-c', command])


def main():
    admin_fixperts_dir = os.path.expanduser('~/dev/fix/admin-fixperts')

    open_terminal_in_dir_with_command(admin_fixperts_dir, 'npm run dev')

    time.sleep(1)

    logs_api_dir = os.path.expanduser('~/dev/fix/fixperts-logs-api')

    open_terminal_in_dir_with_command(logs_api_dir, 'air')

    open_terminal_in_dir_with_command(logs_api_dir, 'bash')


if __name__ == "__main__":
    main()
