import sys

from app import return_data

if len(sys.argv) < 1:
    print('Usage: python main.py city')

city = sys.argv[1]

if __name__ == '__main__':
    return_data(city = city)