"""Create searchable, page-delimited text for the downloaded PDF corpus.
Usage: python extract.py --pdftotext /path/to/pdftotext
The Teen AI PDF has broken font encoding; its separately generated OCR is retained.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--pdftotext', default=shutil.which('pdftotext'))
args = parser.parse_args()
if not args.pdftotext:
    parser.error('Install Poppler or provide --pdftotext /path/to/pdftotext')
root = Path(__file__).parent
rows = json.loads((root / 'corpus_manifest.json').read_text())
for row in rows:
    pdf = root / row['pdf_path']
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == row['sha256']
    if row['id'] == '2026_IJCCI_Landesman_Teen_AI':
        raw = (root / 'ocr_source' / '2026_IJCCI_Landesman_Teen_AI.ocr.txt').read_text()
        pages = re.split(r'===PDF PAGE \d+===', raw)[1:]
        method = 'OCR: Poppler rendering at 180 dpi, Tesseract English --psm 3; original PDF font encoding was unusable.'
    else:
        result = subprocess.run([args.pdftotext, '-enc', 'UTF-8', str(pdf), '-'], check=True, capture_output=True)
        pages = result.stdout.decode('utf-8', errors='replace').split('\f')
        if not pages[-1].strip():
            pages.pop()
        method = 'Poppler pdftotext default reading order, UTF-8.'
    assert len(pages) == row['pdf_pages'], (row['id'],len(pages),row['pdf_pages'])
    header = (f"SOURCE PDF: ../{row['pdf_path']}\nSOURCE URL: {row['pdf_url']}\n"
              f"DOWNLOADED: {row['downloaded_on']}\nEXTRACTION: {method}\n"
              "PAGE NUMBERS: PDF pages, not printed proceedings pages.\n"
              "NOTE: Text may contain OCR, column-order, ligature, hyphenation or figure-label errors. Consult the PDF for quotations and layout.\n")
    text = header + ''.join(f'\n===== PDF PAGE {i} =====\n\n{page.strip()}\n' for i,page in enumerate(pages,1))
    (root / row['txt_path']).write_text(text)
    row['extraction_method'] = method
    row['page_character_counts'] = [len(page.strip()) for page in pages]
    row['extracted_characters'] = sum(row['page_character_counts'])
    row['txt_sha256'] = hashlib.sha256((root / row['txt_path']).read_bytes()).hexdigest()
    print(row['id'], row['pdf_pages'], row['extracted_characters'])
(root / 'corpus_manifest.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
