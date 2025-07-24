import os
import json
from extractor import extract 

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + ".json")

            print(f"📄 Processing: {filename}")
            try:
                result = extract(input_path)  
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"✅ Saved: {output_path}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    main()  #
