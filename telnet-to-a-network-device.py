# telnet-to-a-network-device.py 
# Import required modules/packages/library
import pexpect

# Define variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

# Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('---FAILURE! entering username: ', username)
    exit()

# Session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('----FAILURE! entering password: ', password)
    exit()

# Display a success message if it works
print('----------------------------------')
print('')
print('---- success! connecting to: ', ip_address)
print('-------       Username: ', username)
print('-----        Password: ', password)
print('')
print('------------------------------------')

# Terminate telnet to device and close session
from .exceptions import EOF, TIMEOUT
from .pty_spwan import spawn

def run(command, timeout=30, withexistatus=False, events=None, extra_args=None, logfile=None, cwd=None, env=None, **kwargs) :
if timeout == -1:
    child =spawn(command, maxread=2000, logfile=logfile, cwd=cwd, env=env, **kwargs)
if isinstance(events, list):
    patterns= [x for x,y in events]
    responses = [y for x,y in events]
elif isinstance(events, dict):
    patterns = list(events.keys())
    responses = lists(events.values())
else:
    # This assumes EOF or TIMEOUT will eventually cause run to terminate.
    patterns = None
    responses = None
child_result_list = []
event_count = 0


session.sendline('quit')
session.close()
