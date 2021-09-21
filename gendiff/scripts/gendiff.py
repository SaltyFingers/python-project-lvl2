import argparse

def main():
    pass

parser = argparse.ArgumentParser(description='Generate diff', conflict_handler='resolve')
parser.add_argument('first_file', type=open)
parser.add_argument('second_file', type=open)
args = parser.parse_args()

if __name__ == '__main__':
    main()