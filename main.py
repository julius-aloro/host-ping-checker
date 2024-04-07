# MINI PROJECT: TEST NETWORK CONNECTIONS


import subprocess

with open(r'hosts.txt', 'r+') as f:
    # Read the contents of the 'hosts.txt' as a list (assuming hosts.txt is in same dir)
    ip_addresses = f.read().splitlines()

# Initializing an empty variable to display the summary of the Reachable and Unreachable IP's at script end.
final_out = ''

# Initialize a for loop for each ip to test connectivity
for ip in ip_addresses:
    try:
        command = f'ping -n 1 {ip}'
        output = subprocess.check_output(command.split())
        print(output.decode())
    
    # Allow the script to continue if exception error is encoutered (or if cannot ping the current host)
    except Exception as e:
        print(f'Cannot ping {ip} {e}! Continuing to next IP...')
        print('#' * 100)
        final_out += f'{ip} <-- Unreachable\n'
        continue

    # Execute this code if current host is pingable / alive.
    else:
        print(f'{ip} is alive! ')
        print('#' * 100)
        final_out += f'{ip} <-- Reachable\n'

    # Execute code block after testing all IP in the hosts.txt file, displaying the summary as well.
    finally:
        if ip == ip_addresses[-1]:
            print(f'Script is done running. Below are the results:\n')
            print(final_out)
            print('#' * 100)
            print('exiting script...')
    # END OF SCRIPT
