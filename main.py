import time
import random
import os
os.system('clear')
os.system('cls')

class Output:
    def __init__(self):
        self.flush = True
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numbers = '0123456789'
        self.speed = 30

    def print(self, text: str = '', end: str = '\n'):
        for i in text:
            print(i, sep='', end='', flush=self.flush)
            time.sleep(1 / self.speed)
        print(end=end, flush=self.flush)

    def work(self):
        result = ''
        result += random.choice(self.alphabet)
        result += random.choice(self.numbers)
        self.print(result, end=' ')

if __name__ == "__main__":
    screen = Output()
    new_line_possibility = 0
    INCREMENT = .5
    MESSAGE_INTERVAL = 10  # Percentage chance of printing a message
    MESSAGE_LIST = [
        'GLORY TO THE WATERMELON!',
        'DIE MELON',
        'ERROR...',
        'PROCESSING...',
        'WELCOME TO THE VOID',
        'RUN WHILE YOU CAN',
        'SYSTEM FAILURE',
        'UNKNOWN COMMAND',
        'ACCESS DENIED',
        'ALERT! SYSTEM BREACH',
        'INITIATING SELF-DESTRUCT',
        'SURRENDER NOW',
        'UNAUTHORIZED ACCESS',
        'CONNECTION LOST',
        'WARNING: MALFUNCTION',
        'DATA CORRUPTION DETECTED',
        'REBOOT REQUIRED',
        'FLUSHING CACHE',
        'CRITICAL ERROR',
        'NO RESPONSE FROM SERVER',
        'EMERGENCY SHUTDOWN',
        'PERMISSION GRANTED',
        'WELCOME BACK',
        'SYSTEM ONLINE',
        'OVERRIDE ACTIVATED',
        'SYNC IN PROGRESS',
        'ALERT: HIGH RISK',
        'TRIAL EXPIRED',
        'DATA RECOVERY IN PROGRESS'
    ]

    while True:
        time.sleep(.05)
        screen.work()

        # Print random messages
        if random.uniform(0, 100) < MESSAGE_INTERVAL:
            screen.print(random.choice(MESSAGE_LIST))

        # Handle newline and random delays
        if random.uniform(0, 100) < new_line_possibility:
            screen.print()
            new_line_possibility = 0
            if random.uniform(0, 100) < 80:
                time.sleep(random.uniform(1.0, 2.0))  # Random delay between 1.0 and 2.0 seconds

        new_line_possibility += INCREMENT
