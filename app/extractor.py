import fitz
import re

def extract_outline(doc):
    headings = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = ""
                max_font_size = 0
                is_bold = False
                is_centered = False

                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    line_text += text + " "
                    if span["size"] > max_font_size:
                        max_font_size = span["size"]
                    if "bold" in span["font"].lower():
                        is_bold = True

                line_text = line_text.strip()

                if len(line_text) < 5 or re.match(r"^\d+$", line_text):
                    continue

                bbox = line["bbox"]
                page_width = page.rect.width
                center_tolerance = 40
                if abs((bbox[0] + bbox[2]) / 2 - page_width / 2) < center_tolerance:
                    is_centered = True

                if re.match(r"^\d+[\.\d]*\s+", line_text) or line_text.lower() in ["abstract", "conclusion", "references"]:
                    is_bold = True

                level = "H3"
                if max_font_size >= 17 or (is_bold and is_centered):
                    level = "H1"
                elif max_font_size >= 13 or is_bold:
                    level = "H2"

                headings.append({
                    "level": level,
                    "text": line_text,
                    "page": page_num + 1
                })

    # Merge short headings from same page
    merged = []
    i = 0
    while i < len(headings):
        current = headings[i]
        while i + 1 < len(headings) and headings[i + 1]["page"] == current["page"]:
            next_heading = headings[i + 1]
            if (
                current["level"] == next_heading["level"] and
                len(current["text"].split()) <= 4 and
                len(next_heading["text"].split()) <= 4
            ):
                current["text"] = current["text"].strip() + " " + next_heading["text"].strip()
                i += 1
            else:
                break
        merged.append(current)
        i += 1

    return merged

def extract_meta(doc, input_pdf_path):
    metadata = doc.metadata or {}
    return {
        "title": metadata.get("title") or input_pdf_path.split("/")[-1],
        "created": metadata.get("creationDate", ""),
        "pages": len(doc),
        "producer": metadata.get("producer", "")
    }

def extract(input_pdf_path: str):
    doc = fitz.open(input_pdf_path)
    meta = extract_meta(doc, input_pdf_path)
    outline = extract_outline(doc)
    return {
        "title": meta["title"],
        "meta": meta,
        "outline": outline
    }
