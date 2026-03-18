from PIL import Image
from services.ocr import extract_text_from_image
from services.llm_normalizer import normalize_ingredients_from_ocr
from backend.analyzer import analyze_ingredients, load_db

img = Image.open("sample.jpeg")
ocr_text = extract_text_from_image(img)

ingredients = normalize_ingredients_from_ocr(ocr_text)

db = load_db("ingredients.json")

result = analyze_ingredients(
    ingredients_list=ingredients,
    db=db,
    skin_type="Sensitive"
)

print("FINAL SAFETY SCORE:", result["summary"]["safety_score"])
print("FLAGGED INGREDIENTS:", result["summary"]["flagged_items"])
