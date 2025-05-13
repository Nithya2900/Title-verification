from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import jellyfish
from fuzzywuzzy import fuzz

app = Flask(__name__)
CORS(app)

# MongoDB Connection
client = MongoClient("mongodb+srv://nithya005:nithyasri@cluster0.8xwkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["project"]
raw_data = db["raw_data"]
processed_data = db["processed_data"]
title_similarity = db["title_similarity"]

# Disallowed words and suffixes
DISALLOWED_WORDS = {"Police", "Crime", "Corruption", "CBI", "CID", "Army", "Daily", "Weekly"}
DISALLOWED_PREFIXES_SUFFIXES = {"The", "India", "Samachar", "News"}

def get_similarity_scores(new_title, existing_title):
    """Compute similarity metrics between titles"""
    lev_dist = jellyfish.levenshtein_distance(new_title.lower(), existing_title.lower())
    jaccard_sim = len(set(new_title.lower().split()) & set(existing_title.lower().split())) / len(set(new_title.lower().split()) | set(existing_title.lower().split()))
    
    # Compute phonetic similarity
    soundex_sim = 1 if jellyfish.soundex(new_title) == jellyfish.soundex(existing_title) else 0
    metaphone_sim = 1 if jellyfish.metaphone(new_title) == jellyfish.metaphone(existing_title) else 0
    phonetic_sim = max(soundex_sim, metaphone_sim)

    overall_similarity = max((1 - lev_dist / max(len(new_title), len(existing_title))) * 100, jaccard_sim * 100, phonetic_sim * 100)
    
    return overall_similarity, lev_dist, jaccard_sim, phonetic_sim

@app.route("/check_title", methods=["POST"])
def check_title():
    data = request.json
    new_title = data.get("title", "").strip()

    if not new_title:
        return jsonify({"error": "Title cannot be empty"}), 400

    # Check for violated words
    violated_words = [word for word in DISALLOWED_WORDS if word.lower() in new_title.lower()]
    
    # Fetch existing titles from DB
    existing_titles = [doc["Title Name"] for doc in raw_data.find({}, {"Title Name": 1})]

    best_match = None
    highest_similarity = 0

    # Compare with each title
    for existing_title in existing_titles:
        similarity, lev_dist, jaccard_sim, phonetic_sim = get_similarity_scores(new_title, existing_title)

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = existing_title

    verification_probability = max(0, 100 - highest_similarity)

    # Assign color-coded status
    if verification_probability >= 70:
        status = "✅ Green - Highly Unique"
    elif 40 <= verification_probability < 70:
        status = "⚠️ Yellow - Moderately Similar"
    else:
        status = "❌ Red - Highly Similar or Disallowed"
    
    return jsonify({
        "title": new_title,
        "similar_titles": [{"title": best_match, "similarity_score": round(highest_similarity, 2)}] if best_match else [],
        "violated_words": violated_words,
        "verification_probability": round(verification_probability, 2),
        "status": status
    })

if __name__ == "__main__":
    app.run(debug=True)
