import time
import random


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
    for i in range(50):
        time.sleep(.05)
        screen.work()
        if random.uniform(0, 100) < 10:
            screen.print(random.choice(['GLORY TO THE WATERMELON!',
                                        'DIE MELON',
                                        'ERROR...',
                                        'PROCESSING...']))

        if random.uniform(0, 100) < new_line_possibility:
            screen.print()
            new_line_possibility = 0
            if random.uniform(0, 100) < 80:
                time.sleep(1.5)

        new_line_possibility += INCREMENT