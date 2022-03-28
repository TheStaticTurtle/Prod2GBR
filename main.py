import argparse
import pathlib
import sys

import manufacturers
import logging

logging.basicConfig(stream=sys.stdout)

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", help="Input file", required=True)
parser.add_argument("--manufacturer", "-m", help="Manufacturer to use", choices=manufacturers.manufacturers_list, required=True)
parser.add_argument("--output", "-o", help="Output file (Default to {input-file-name}-gbr.zip)")

args = parser.parse_args()

logging.info("Hellow world")
logging.info(f"Reading {args.input} with {manufacturers.manufacturers[args.manufacturer].__class__.__name__}")

k = manufacturers.manufacturers[args.manufacturer]()

try:
    result = k.process(args.input)
    logging.info(f"Done, result at: {result}")

except Exception as e:
    logging.error(e)