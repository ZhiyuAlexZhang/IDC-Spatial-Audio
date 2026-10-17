CDY-related empirical papers and comparison with the spatial-audio findings
Collected and reviewed: 17 October 2026

START HERE
1. comparison_with_findings_v5.txt: the comparative assessment and revision priorities.
2. bibliography.txt: all 18 papers, authors, venues, DOIs, source URLs and local paths.
3. review_notes/: detailed paper-by-paper readings with findings headings and page locators.
4. pdf/: 18 original public PDFs, unchanged.
5. txt/: 18 searchable, page-delimited UTF-8 text files.
6. corpus_manifest.json: structured bibliography, sources, hashes, page counts and extraction methods.

SCOPE
An author-centered, purposive comparison corpus spanning publication years 2020-2026,
selected from public papers involving Jason Yip, Katie Davis, Aayushi Dangol, Rotem
Landesman and collaborators associated with the UW Center for Digital Youth community.
It is not an exhaustive institutional bibliography and does not claim every paper was
formally submitted on behalf of CDY. It contains publicly available published papers
and author manuscripts, not confidential submissions, reviews or rejected papers.

11 IDC publications: nine full research papers, one empirical pictorial (Metaphor
Sandwich), and one empirical work-in-progress poster paper (BIG TROUBLE).
Seven contextual comparators: four CHI research papers, one DIS research paper,
one ISMIR research paper and one IJCCI journal research paper.
Different venues, genres, age groups and methods are identified in the notes.
The two NatureCollections papers analyze a shared larger study, not independent replications.

SELECTION AND REVIEW
Priority went to empirical youth/co-design papers with accessible full text and useful
comparisons for findings structure, design-artifact presentation, technology sensemaking,
embodied interaction, or adolescent judgments. All 18 findings sections were reviewed;
methods and discussions were inspected to interpret them. Relevant artifact/table/model
pages were visually checked. Three independent review assignments covered Yip, Davis/
Landesman and Dangol; the integrated report checks their implications against the current
4-findings.tex. This is a comparative reading, not a systematic review or an acceptance model.

PRIMARY DISCOVERY SOURCES
https://www.kidsteam.ischool.uw.edu/publications
https://bigyipper.com/articles-publications/
https://katiedavisresearch.com/
https://adango26.github.io/publication.html
https://digitalyouth.uw.edu/people/
Public author pages, university pages, proceedings metadata and author-hosted full texts
were used. Exact download URLs are recorded per paper.

TEXT QUALITY
Most text uses Poppler pdftotext default reading order, UTF-8. Form-feed boundaries are
replaced by explicit PDF page markers. PDF page 1 means the first page of the downloaded
file, not the printed proceedings page. Columns, diagrams, handwriting, ligatures and
hyphenation can introduce errors. Images are not fully transcribed. Consult the PDF before
quoting or making layout claims.
The IJCCI 2026 Teen AI PDF has broken font encoding. Its txt file instead uses labeled OCR:
Poppler render 180 dpi, Tesseract English --psm3, all 16 pages. The OCR source is retained in
ocr_source/. It is readable but not a manually corrected transcription.

SOURCE CORRECTIONS
- The author-page link25_idc3.pdf beside BIG TROUBLE actually served AI Puzzlers.
  It was excluded and replaced by the correct six-page arXiv2505.16089 manuscript.
- AI Toys uses the final 17-page IDC 2026 author copy. The older 16-page preprint with
  an erroneous Conference17 footer was excluded.
- Metaphor Sandwich uses the April 2024 author copy; it is a pictorial.
- The Purrble author copy ends its title with Devices, whereas the indexed title uses Device.
  Its24-page pagination differs from other versions.
- Locus is indexed under its published title, without the extra author-website subtitle.

PROVENANCE AND REUSE
Original PDFs retain their authorship, copyright and license notices. Public availability
does not itself give every file the same reuse license. This collection does not relicense
third-party work. Text files are extraction aids, not new authoritative versions.

REPRODUCTION
python3 download.py
python3 extract.py --pdftotext /path/to/pdftotext
The download script reads sources.json and verifies PDF magic before recording hashes.
The extraction script checks each PDF against corpus_manifest.json and uses the retained
OCR source for Teen AI. Re-running download.py may retrieve changed source versions;
check any hash changes before replacing this reviewed snapshot.
