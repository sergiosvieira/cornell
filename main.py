import argparse
import pymupdf


def process_pdf(input_file, output_file, position):
    # Open the PDF document
    doc = pymupdf.open(input_file)

    # Double the number of pages by duplicating each page
    # selected = [x for x in range(doc.page_count) for _ in range(2)]
    # doc.select(selected)

    # Define rectangle coordinates and dimensions
    lx = 0
    rx = 306
    top = 45
    height = 705

    # Iterate over each page in the document
    for page_index in range(doc.page_count):
        page = doc[page_index]  # Get the current page
        
        # Define the rectangle and image based on the page index (0-based indexing)
        if page_index % 2 == 0 and position == "right":  # Even pages (original odd pages)
            r_str = "retangulo_white.png"
            r = pymupdf.Rect(rx, top, rx + 306, top + height)
        elif position == "left":  # Odd pages (original even pages)
            r_str = "retangulo_white.png"
            r = pymupdf.Rect(lx, top, lx + 305, top + height)
        
        # Insert the image into the page
        page.insert_image(r, filename=r_str, overlay=True, keep_proportion=False)

    # Save the modified document with a new filename
    doc.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a PDF file to add rectangles on specified sides.")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_pdf", help="Path to the output PDF file")
    parser.add_argument("position", choices=['left', 'right'], help="Position of the rectangle ('left' or 'right')")

    args = parser.parse_args()
    
    process_pdf(args.input_pdf, args.output_pdf, args.position)