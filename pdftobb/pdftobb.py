import sys
import os

from bs4 import BeautifulSoup
from pdftobb.combine_textboxes import extract_textboxes


def run_pdftobb():
    fn = sys.argv[1]
    outn = fn + '.xml'
    csvn = fn + '.csv'
    os.system("pdf2txt.py -t xml {} > {}".format(fn, outn))

    soup = BeautifulSoup(open(outn).read(), 'lxml')
    df = extract_textboxes(soup)

    df.to_csv(csvn, index=False)


if __name__ == '__main__':
    run_pdftobb()
