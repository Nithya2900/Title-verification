# Automated Title Verification System - VerifyPro

_A Smart India Hackathon (SIH) 2025 Project – Solution to Problem Statement 1782_

## 📌 Problem Statement

**Title Verification Automation**  
The system addresses the need to automate the verification of newly submitted newspaper or journal titles by ensuring uniqueness, compliance with predefined rules, and prevention of duplicate or misleading names.

Manual methods are time-consuming, inconsistent, and prone to errors. This system eliminates redundancy by employing phonetic and semantic similarity detection along with strict rule-based validation.

---

## 🎯 Objectives & Goals

- ✅ Ensure **uniqueness** of all new title submissions.
- ✅ Detect **phonetic**, **spelling**, and **semantic** similarities.
- ✅ Reject titles with **disallowed words**, **prefixes**, or **suffixes**.
- ✅ Prevent names created by combining or modifying existing titles.
- ✅ Provide a **probability score** indicating the chance of title acceptance.
- ✅ Offer **clear feedback** for rejected submissions to enable corrections.
- ✅ Maintain **scalability** to support large volumes (160K+ titles).
- ✅ Optimize **database search** for speed and performance.

---

## 🔍 Existing Systems & Limitations

| Current Approach | Drawbacks |
|------------------|-----------|
| Manual Review | Time-consuming, inconsistent |
| String Matching | Fails for phonetic variations (e.g., _Samachar_ vs. _Samaachar_) |
| No Standardization | Lack of rules for prefixes/suffixes |
| No Scoring System | Users get no clarity on rejection reasons |

---

## 💡 Proposed Solution

We propose a **multi-layered verification system** combining:

- **Phonetic Matching:** Using algorithms like Soundex and Metaphone.
- **Semantic Similarity:** Leveraging NLP models (e.g., Word2Vec, BERT).
- **Rule-Based Filtering:** Custom logic to reject disallowed structures or combinations.
- **Indexed Database Search:** For fast, scalable title lookups.
- **User Interface:** For submitting titles and viewing probability scores and feedback.

---

## ⚙️ Technology Stack

| Component | Technology |
|----------|------------|
| Backend | Python / Node.js |
| NLP & Similarity | Word2Vec, BERT, Soundex, Metaphone |
| Database | MongoDB / PostgreSQL (with indexing) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker / Cloud (Optional) |

---

## 🧪 Key Functionalities

- **Similarity Detection Module**
  - Phonetic checks (e.g., "Namaskar" vs "Namascar")
  - Semantic similarity using NLP embeddings

- **Rule-Based Validator**
  - Rejects if disallowed words/prefixes/suffixes are present
  - Disallows combinations like “Hindu Indian Express”

- **Verification Score Engine**
  - Returns a confidence score (0-100%) indicating how likely a title is to be accepted

- **User Feedback System**
  - Explains rejection reasons
  - Allows resubmission with suggestions

- **Optimized Title Search**
  - Indexed lookups for fast title comparison (160K+ entries supported)

---

## 🔮 Future Enhancements

- 🔤 Add **multilingual support** for title comparison
- 🤖 Integrate **advanced AI models** like Sentence-BERT
- 🌐 Create a **responsive web interface**
- ⚙️ Enable **bulk title uploads** and report generation
- 📊 Provide **analytics dashboard** for admin insights

---

<img src="https://github.com/user-attachments/assets/8fa6f54b-bad7-40b2-a9ed-63fa48ea7fc5" width="600"/>
<img src="https://github.com/user-attachments/assets/e3562aab-152d-4746-a430-dbc7215a0fcc" width="600"/>
<img src="https://github.com/user-attachments/assets/819baa29-8f88-45e3-ba63-43ac9752aff6" width ="600"/>
<img src="https://github.com/user-attachments/assets/7163f13b-2cab-4787-98e6-9cc17e307e25" width="600"/>

---

## 📝 References

- Soundex & Metaphone Algorithms – [Wikipedia](https://en.wikipedia.org/wiki/Soundex)
- NLP Semantic Models – Word2Vec, BERT
- Database Indexing – B-Trees, Hash Indexing, Full-Text Search
- Real-World Use Cases – Title Validation in Publishing Industries






