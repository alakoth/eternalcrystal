from main import generate
import argparse 
parser = argparse.ArgumentParser(description='ETERNALCRYSTAL - Generate codenames on the fly.')
parser.add_argument('-w', metavar='--wordlist', type=str, nargs='?',help='path to wordlist')
args = parser.parse_args()
file = f'{args.w}'
generate(file)