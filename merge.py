import argparse
import pymupdf
import operator
from functools import reduce

def merge_pdf(first, second, output):
    doc_left = pymupdf.open(first) # open the 1st document
    doc_right = pymupdf.open(second) # open the 2nd document
    doc_right.insert_file(doc_left) # merge the docs
    left_selected = list(range(0, doc_left.page_count))
    right_selected = list(range(doc_left.page_count, doc_right.page_count))
    selected = reduce(operator.add, zip(left_selected, right_selected))
    doc_right.select(selected)
    doc_right.save(output) # save the merged document with a new filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDF file.")
    parser.add_argument("first_pdf", help="Path to the first PDF file.")
    parser.add_argument("second_pdf", help="Path to the second PDF file.")
    parser.add_argument("output_pdf", help="Path to the output PDF file.")
    args = parser.parse_args()    
    merge_pdf(args.first_pdf, args.second_pdf, args.output_pdf)