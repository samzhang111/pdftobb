# pdftobb

General PDF parsing code extracted from my [newspaper mining codebase](http://github.com/samzhang111/frontpages).

This uses pdfminer3k to dump a PDF file as an XML file. Then it collates bounding boxes and outputs a (pandas-style) CSV.

## Installation
### Via pip
1. Initialize a virtual environment
2. `pip install pdftobb`

### Via git

1. Clone this repository, `cd` to it
2. Initialize a virtual environment, activate it
3. `pip install -r requirements.txt`

## Usage:
If installed via pip: `pdftobb path/to/pdf.pdf`

If installed locally: `python path/to/pdftobb.py path/to/pdf.pdf`

Running `pdftobb` on a file `file.pdf` will generate two files: `file.pdf.xml` (the output of `pdf2txt.py -t xml file.pdf > file.pdf.xml`) and `file.pdf.csv`, which is the XML file turned into a slightly more condensed csv file.
