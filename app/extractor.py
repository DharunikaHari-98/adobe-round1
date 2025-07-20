import fitz  # PyMuPDF

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    font_size_map = {}

    title = ""
    max_font_size = 0
    title_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]

                    if not text:
                        continue

                    # Track the largest font size for Title
                    if size > max_font_size and page_num == 0:
                        max_font_size = size
                        title_text = text

                    # Build a font size map to guess heading levels
                    if size not in font_size_map:
                        font_size_map[size] = []
                    font_size_map[size].append({
                        "text": text,
                        "page": page_num + 1,
                        "size": size
                    })

    # Sort font sizes descending to determine H1 > H2 > H3
    sorted_sizes = sorted(font_size_map.keys(), reverse=True)
    heading_levels = {}

    if len(sorted_sizes) >= 1:
        heading_levels[sorted_sizes[0]] = "H1"
    if len(sorted_sizes) >= 2:
        heading_levels[sorted_sizes[1]] = "H2"
    if len(sorted_sizes) >= 3:
        heading_levels[sorted_sizes[2]] = "H3"

    # Extract headings
    for size in heading_levels:
        for item in font_size_map[size]:
            headings.append({
                "level": heading_levels[size],
                "text": item["text"],
                "page": item["page"]
            })

    return {
        "title": title_text,
        "outline": headings
    }
