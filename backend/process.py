import pymongo
import re
from metaphone import doublemetaphone

# MongoDB Connection with Timeout
try:
    client = pymongo.MongoClient(
        "mongodb+srv://nithya005:nithyasri@cluster0.8xwkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        serverSelectionTimeoutMS=5000  # Timeout in 5000ms (5 seconds)
    )
    db = client["project"]
    raw_collection = db["raw_data"]
    processed_collection = db["processed_data"]
    
    # Test Connection
    client.server_info()  # Triggers a connection attempt

except pymongo.errors.ServerSelectionTimeoutError:
    print("❌ MongoDB Connection Timeout! Please check your internet or database settings.")
    exit()

# Function to clean and normalize text
def clean_text(text):
    text = text.lower().strip()  # Lowercase & trim spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special characters
    return text

# Process raw data and store in processed_data
def process_and_store_data():
    try:
        total_raw = raw_collection.count_documents({})
        print(f"🔄 Processing {total_raw} raw titles...\n")

        for record in raw_collection.find({}, {"Title Name": 1}):
            raw_title = record.get("Title Name", "").strip()

            if not raw_title:
                print("⚠️ Skipping empty title...\n")
                continue

            clean_title = clean_text(raw_title)
            phonetic_code = doublemetaphone(clean_title)[0]

            if not processed_collection.find_one({"clean_title": clean_title}, {"_id": 1}):
                processed_collection.insert_one({
                    "original_title": raw_title,
                    "clean_title": clean_title,
                    "phonetic_code": phonetic_code
                })
                print(f"✅ Stored: '{raw_title}' → '{clean_title}' (Phonetic: {phonetic_code})\n")
            else:
                print(f"🔁 Skipped Duplicate: '{clean_title}' already exists.\n")

        print("✅ Data cleaning & storage completed!")

    except pymongo.errors.PyMongoError as e:
        print(f"❌ MongoDB Error: {e}")

# Run the function
if __name__ == "__main__":
    process_and_store_data()
