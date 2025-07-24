# 🧠 Adobe India Hackathon 2025 - Round 1A Submission

## 📌 Challenge Theme: Connecting the Dots Through Docs

### ✅ Objective
This project extracts a structured **outline (Title + Headings: H1, H2, H3)** from a PDF and outputs the result in a valid JSON format. It is built for **high accuracy**, **fast performance**, and **offline compatibility**, as required in Round 1A.

---

## 📁 Folder Structure

├── app/
│ ├── extractor.py # PDF outline extraction logic
│ └── main.py # Driver script to process all PDFs
├── input/
│ └── discover.pdf # Sample input PDF
├── output/
│ └── discover.json # Output JSON with extracted outline
├── schema/
│ └── output_schema.json # JSON schema reference
├── requirements.txt # Python libraries used
├── Dockerfile # Docker build configuration
├── .dockerignore.txt # Docker ignore rules
└── README.md # Documentation


---

## 🚀 How to Build & Run

### 🔨 Build Docker Image

```bash
docker build --platform linux/amd64 -t adobehack:round1a .


docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none adobehack:round1a

 The script will:

Automatically process all .pdf files inside /app/input

Generate .json output files with outlines in /app/output

Approach
PDF Parsing: We used PyMuPDF (fitz) to extract fonts, positions, and text content.

Heading Detection:

Headings are classified using a combination of font size, font weight, and layout structure.

Hierarchy is determined (H1 > H2 > H3) based on clustering font size patterns within the document.

Title Detection:

The document title is selected from the first page using the largest and boldest text.

Structure Generation:

The extracted headings are stored along with their level and page number in the expected JSON schema.

 Sample Output Format
json
Copy
Edit
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}


Performance & Compatibility
Feature	Status
⏱️ Runtime < 10s	✅ Yes
💻 CPU-only	✅ Yes
🌐 Offline compatible	✅ Yes
🧠 Model size ≤ 200MB	✅ No model used
🧾 JSON schema match	✅ Yes


PyMuPDF==1.23.22
pdfminer.six==20221105
numpy==1.26.4
Installed via requirements.txt.


Constraints Handled
✅ Compatible with linux/amd64

✅ Does not rely on font size only

✅ Generalized logic — no hardcoding

✅ Runs fully offline

✅ No internet/API calls

Submission Checklist
 Dockerfile in root directory

 All code in /app

 README.md with approach + run instructions

 Works with docker run test command

 JSON output matches provided schema

 Handles up to 50 pages in <10s

