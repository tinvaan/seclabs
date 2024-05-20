# pylint: disable-all

import hashlib
import argparse
import timeit
import random

def hashing_md5(s):
    return hashlib.md5(s.encode()).hexdigest()

def dict_attack(input, dict, output):
    # input: <student_id>.txt, dict: words5.txt, output: output_dict.txt
    #Code here
    return 

def brute_force_alpha_numeric(input, output):
    #input: <student_id>.txt, output: output_brute.txt
    #Code here
    return

def add_salt(input,output):
    #input: output_brute.txt, output: salted_hash.txt
    #Code here
    return

def parseArgs():
    """
        Function for arguments parsing
    """
    aparser = argparse.ArgumentParser(
        description='Script demonstrates breaking of simple password: Dictionary Attack and BruteForce.',
        formatter_class=argparse.RawTextHelpFormatter)
    aparser.add_argument('-i', required=True, metavar='INPUT_FILE', help='Filename of the Input File.')
    aparser.add_argument('-w', required=True, metavar='DICT_FILE', help='Filename of the Dictionary File.')
    aparser.add_argument("-o", required=True, metavar='OUTPUT_FILE', help='Filename of the Output File.')
    args = aparser.parse_args()

    return args


def main():
    SETUP_CODE = '''
from __main__ import parseArgs
from __main__ import dict_attack
from __main__ import brute_force_alpha_numeric
from __main__ import add_salt
args = parseArgs()
input_file = args.i
dict_file = args.w
output_file = args.o'''

    print('Please select a Mode:\n')
    print('1 - Dictionary Attack\n')
    print('2 - BruteForce with Lowercase Alphabet and Digits\n')
    print('3 - Add Salt and Hash new Password\n')
    mode = input('Mode: ')

    while not (mode == '1' or mode == '2' or mode == '3'):
        mode = input('Incorrect Mode! Please select a correct Mode: ')
        print(mode)

    if mode == '1':
        RUN_CODE = 'dict_attack(input_file, dict_file, output_file)'
        timing = timeit.timeit(setup=SETUP_CODE, stmt=RUN_CODE, number=1)
        print('Run Completed! Time Taken: ' + str(timing) + ' seconds\n')

    elif mode == '2':
        RUN_CODE = 'brute_force_alpha_numeric(input_file, output_file)'
        timing = timeit.timeit(setup=SETUP_CODE, stmt=RUN_CODE, number=1)
        print('Run Completed! Time Taken: ' + str(timing) + ' seconds\n')

    elif mode == '3':
        RUN_CODE = 'add_salt(input_file, output_file)'
        timing = timeit.timeit(setup=SETUP_CODE, stmt=RUN_CODE, number=1)
        print('Run Completed! Time Taken: ' + str(timing) + ' seconds\n')


if __name__ == '__main__':
    main()
