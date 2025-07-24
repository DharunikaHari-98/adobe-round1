# 🧠 Adobe India Hackathon 2025 - Round 1A Submission

## 📌 Challenge Theme: Connecting the Dots Through Docs

### ✅ Objective
Build an AI-powered assistant that extracts a structured **outline** (Title + Headings H1, H2, H3) from any PDF document. The solution should run **offline**, support **multiple PDFs**, and output in a **valid JSON format**.

---

## 🗂 Folder Structure

├── app/
│ ├── extractor.py # PDF outline extraction logic
│ └── main.py # Driver script to run extraction
├── input/
│ └── discover.pdf # Example input PDF
├── output/
│ └── discover.json # Output JSON with extracted outline
├── schema/
│ └── output_schema.json # JSON schema to validate output
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build config
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 How to Run (Dockerized)

### 🔧 Build Docker Image
```bash
docker build --platform linux/amd64 -t adobehack:round1a .
▶️ Run on PDFs
bash
Copy
Edit
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none adobehack:round1a
All PDFs in /input will be processed

Corresponding .json files will be saved in /output

🧠 Approach
📄 PDF Parsing
Used PyMuPDF to extract text, font sizes, and positions

🔠 Heading Detection
Fonts were clustered to infer heading hierarchy (H1 > H2 > H3)

Structure is extracted without relying solely on font size

🏷️ Title Detection
Extracted from Page 1 using largest and boldest font

📤 Output Format
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
⚙️ Compatibility & Performance
Feature	Status
⏱️ Runtime < 10s	✅ Yes
💻 CPU-only	✅ Yes
🌐 Offline-compatible	✅ Yes
🧠 Model size ≤ 200MB	✅ No model used
🧾 JSON schema match	✅ Yes
📦 Linux/amd64 compatible	✅ Yes

✅ Constraints Handled
✔ Works fully offline

✔ Handles multiple PDFs

✔ No hardcoding

✔ Uses general logic

✔ Meets Adobe's schema

