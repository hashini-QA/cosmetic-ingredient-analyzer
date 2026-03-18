import json

def normalize_key(name: str) -> str:
    return name.strip().lower()

def load_db(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        raw_db = json.load(f)

    normalized_db = {}
    for _, data in raw_db.items():
        inci = data.get("inci_name")
        if inci:
            normalized_db[normalize_key(inci)] = data
    return normalized_db


def analyze_ingredients(ingredients_list, db, skin_type):
    flagged = []
    total_comed = 0
    details = []

    for ing in ingredients_list:
        key = normalize_key(ing)
        ing_data = db.get(key, {
            "category": "Unknown",
            "benefits": "No data",
            "risk": "Low",
            "comedogenic": 0
        })

        if ing_data["risk"] in ["Medium", "High"]:
            flagged.append({
                "name": ing,
                "risk": ing_data["risk"],
                "comedogenic": ing_data["comedogenic"]
            })

        total_comed += ing_data["comedogenic"]

        details.append({
            "Ingredient": ing,
            "Category": ing_data["category"],
            "Benefits": ing_data["benefits"],
            "Risk": ing_data["risk"],
            "Comedogenic": ing_data["comedogenic"]
        })

    avg_comed = round(total_comed / len(ingredients_list), 2) if ingredients_list else 0
    safety_score = calculate_safety(ingredients_list, db, skin_type)

    return {
        "summary": {
            "safety_score": safety_score,
            "avg_comedogenic": avg_comed,
            "flagged_items": flagged
        },
        "details": details
    }


def calculate_safety(ingredients_list, db, skin_type):
    score = 0

    for ing in ingredients_list:
        ing_data = db.get(normalize_key(ing), {"risk": "Low", "comedogenic": 0})
        risk = ing_data["risk"]
        comed = ing_data["comedogenic"]

        if skin_type == "Oily":
            score += comed * 2
            if risk in ["Medium", "High"]:
                score += 2
        elif skin_type == "Sensitive":
            if risk in ["Medium", "High"]:
                score += 3
        else:
            score += comed

    max_score = max(len(ingredients_list) * 5, 1)
    return max(0, 100 - int(score / max_score * 100))
