import os
import json
from extractor import extract_outline_from_pdf  # ✅ Corrected import

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Processing: {filename}")
            try:
                result = extract_outline_from_pdf(input_path)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"Saved: {output_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
