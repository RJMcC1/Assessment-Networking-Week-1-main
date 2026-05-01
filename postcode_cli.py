"""A CLI application for interacting with the Postcode API."""

from argparse import ArgumentParser
import argparse
from postcode_functions import validate_postcode , get_postcode_completions , load_cache , save_cache


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", choices= ["validate" , "complete"], required=True)
    parser.add_argument("postcode")
    args = parser.parse_args()
    if args.mode == "validate":
        valid = validate_postcode(args.postcode)
        if valid == False:
            print( f'{args.postcode.upper().strip()} is not a valid postcode.')
        if valid == True:
            print(f'{args.postcode.upper().strip()} is a valid postcode.')
    if args.mode == "complete":
        postcode = args.postcode.strip().upper()
        completions = get_postcode_completions(postcode)
        if not completions:
            print(f"No matches for {postcode}.")
        else:
            for completion in completions[:5]:
                print(f"{completion.upper()}.")
    
    
