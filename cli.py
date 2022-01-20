from main import generate
import argparse 
parser = argparse.ArgumentParser(description='ETERNALCRYSTAL - Generate code names on the fly.')
parser.add_argument('-w', metavar='--wordlist', type=str, nargs='?',help='path to wordlist')
parser.add_argument('-v', '--version', action='version', version='v0.0.1-alpha', help='print version')
args = parser.parse_args()
file = f'{args.w}'
generate(file)
