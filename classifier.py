def classify_document(text):

    if not text:
        return "Others"

    text = text.lower()

    keywords = {
        "Resume": [
            "curriculum vitae",
            "resume",
            "education",
            "skills",
            "experience",
            "certification",
            "career objective"
        ],

        "Invoice": [
            "invoice",
            "bill",
            "gst",
            "payment",
            "amount due",
            "tax invoice"
        ],

        "Report": [
            "abstract",
            "introduction",
            "methodology",
            "literature review",
            "results",
            "discussion",
            "conclusion",
            "references",
            "analysis",
            "report"
        ],

        "Notes": [
            "normalization",
            "primary key",
            "foreign key",
            "database",
            "sql",
            "dbms"
        ]
    } 

    scores = {}

    for category, words in keywords.items():
        scores[category] = 0
        for word in words:
            if word in text:
                scores[category] += 1

    # Find category with highest score
    best_category = max(scores, key=scores.get)

    # If no keywords matched
    if scores[best_category] == 0:
        return "Others"

    return best_category