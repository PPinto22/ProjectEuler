import millerRabin as mr
import timer

def main():
    diagonals = [1]
    primes = []
    square_root = 3
    while True:
        oddSquare = square_root ** 2
        diagonals.append(oddSquare)
        for i in range(1, 4):
            diagonalNumber = oddSquare - (square_root-1) * i
            diagonals.append(diagonalNumber)
            if mr.is_prime(diagonalNumber):
                primes.append(diagonalNumber)
        ratio = len(primes) / float(len(diagonals))
        # print str(square_root) + ": " + str(ratio)
        if ratio < 0.10:
            break
        square_root += 2
    print square_root


if __name__ == '__main__':
    timer.run(main)
