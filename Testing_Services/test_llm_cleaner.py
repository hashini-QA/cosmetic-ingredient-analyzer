from services.llm_normalizer import normalize_ingredients_from_ocr

ocr_text = """
INGREDIENTS: WATER, CETYL ALCOHOL, PROPYLENE GLYCOL,
SODIUM LAURYL SULFATE, STEARYL ALCOHOL,
METHYLPARABEN, PROPYLPARABEN, BUTYLPARABEN
"""

ingredients = normalize_ingredients_from_ocr(ocr_text)

print("CLEAN INGREDIENTS:")
for ing in ingredients:
    print("-", ing)
