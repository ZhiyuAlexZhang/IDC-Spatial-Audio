import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request

root = Path(__file__).parent
rows = json.loads((root / 'sources.json').read_text())

def download(row):
    path = root / 'pdf' / (row['id'] + '.pdf')
    try:
        if path.exists() and path.read_bytes().startswith(b'%PDF'):
            data = path.read_bytes()
            final_url = row['pdf_url']
        else:
            req = urllib.request.Request(row['pdf_url'], headers={'User-Agent': 'Mozilla/5.0 (research literature retrieval)'})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
                final_url = response.url
            if not data.startswith(b'%PDF'):
                raise ValueError('Response is not a PDF')
            path.write_bytes(data)
        return dict(row, status='downloaded', resolved_url=final_url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), downloaded_on='2026-10-17')
    except Exception as error:
        return dict(row, status='failed', error=str(error))

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(download, rows))
(root / 'download_manifest.json').write_text(json.dumps(results, indent=2))
for row in results:
    print(row['id'], row['status'], row.get('bytes', row.get('error')))
