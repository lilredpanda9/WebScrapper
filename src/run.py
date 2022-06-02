import constants as c
import main

# minimal file, runs entire project

def run():
        primes = main.calculate_primes(c.START, c.FINISH)
        print(primes)

if __name__ == '__main__':
    run()