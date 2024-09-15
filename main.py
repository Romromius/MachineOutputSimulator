import os
import random
import subprocess
import sys
import time


def check_for_updates():
    # Fetch updates from remote without merging
    subprocess.run(["git", "fetch"], check=True)

    # Check if local branch is behind remote
    status = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)

    if "Your branch is behind" in status.stdout:
        return True
    return False


def pull_updates():
    # Pull updates from remote repository
    subprocess.run(["git", "pull"], check=True)


def main():
    if 'linux' in sys.platform:
        os.system('clear')
    elif 'win' in sys.platform:
        os.system('cls')
    space = 0
    while True:
        for i in range(80):
            if space > random.uniform(0, 2):
                print(' ', end='', flush=True)
                space = 0
            else:
                print(random.choice('1234567890qwertyuiopasdfghjklzxcvbnnm'.upper()), end='', flush=True)
                space += .1
            time.sleep(0.05)
        time.sleep(random.uniform(1.0, 2.0))  # Random delay between 1.0 and 2.0 seconds
        print()


if __name__ == "__main__":
    try:
        update_avalible = check_for_updates()
    except subprocess.CalledProcessError:
        print('No network connection.')
        update_avalible = False
    if update_avalible:
        print("Updates found! Pulling updates...")
        pull_updates()
        # After pulling updates, just run main.py
        print("Running updated main.py...")
        main()
    else:
        print("No updates found, running main.py...")
        main()
