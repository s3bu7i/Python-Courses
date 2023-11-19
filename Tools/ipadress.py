import subprocess

def get_connected_devices():
    result = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE)
    return result.stdout.decode()

print(get_connected_devices())