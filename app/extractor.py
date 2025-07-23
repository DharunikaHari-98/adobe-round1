import fitz  # PyMuPDF

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    font_style_map = {}

    title_text = ""
    max_font_size = 0

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
                    flags = span["flags"]  # Bold/italic detection
                    bbox = span["bbox"]
                    alignment = "center" if abs((bbox[0] + bbox[2]) / 2 - page.rect.width / 2) < 50 else "left"

                    if not text or len(text) < 2:
                        continue

                    # Track largest font size for Title
                    if size > max_font_size and page_num == 0:
                        max_font_size = size
                        title_text = text

                    # Store text metadata
                    if size not in font_style_map:
                        font_style_map[size] = []
                    font_style_map[size].append({
                        "text": text,
                        "page": page_num + 1,
                        "size": size,
                        "bold": bool(flags & 2),
                        "italic": bool(flags & 1),
                        "alignment": alignment
                    })

    # Determine heading levels (H1 > H2 > H3)
    sorted_sizes = sorted(font_style_map.keys(), reverse=True)
    heading_levels = {}

    if len(sorted_sizes) >= 1:
        heading_levels[sorted_sizes[0]] = "H1"
    if len(sorted_sizes) >= 2:
        heading_levels[sorted_sizes[1]] = "H2"
    if len(sorted_sizes) >= 3:
        heading_levels[sorted_sizes[2]] = "H3"

    # Extract headings with additional cues
    for size in heading_levels:
        for item in font_style_map[size]:
            is_heading = (
                item["bold"] or
                item["alignment"] == "center" or
                len(item["text"].split()) <= 10  # Short text likely heading
            )
            if is_heading:
                headings.append({
                    "level": heading_levels[size],
                    "text": item["text"],
                    "page": item["page"]
                })

    return {
        "title": title_text,
        "outline": headings
    }
