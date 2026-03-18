import json
from db.models import AnalysisResult

def save_analysis_result(
    db_session,
    user_email: str,
    skin_type: str,
    product_name: str,
    brand: str,
    raw_ingredients_text: str,
    normalized_ingredients: list[str],
    safety_score: int,
    flagged_items: list[dict],
):
    row = AnalysisResult(
        user_email=user_email,
        skin_type=skin_type,
        product_name=product_name,
        brand=brand,
        raw_ingredients_text=raw_ingredients_text,
        normalized_ingredients=json.dumps(normalized_ingredients, ensure_ascii=False),
        safety_score=safety_score,
        flagged_ingredients=json.dumps(flagged_items, ensure_ascii=False),
    )
    db_session.add(row)
    db_session.commit()
    db_session.refresh(row)
    return row
