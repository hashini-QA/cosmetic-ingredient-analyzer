import json
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
Extract ONLY cosmetic ingredient names.
Ignore marketing text and directions.
Return STRICT JSON only.

Format:
{
  "ingredients": ["Water", "Glycerin"]
}
"""

def normalize_ingredients_from_ocr(text: str) -> list[str]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    try:
        data = json.loads(response.choices[0].message.content)
        return data.get("ingredients", [])
    except json.JSONDecodeError:
        return []
