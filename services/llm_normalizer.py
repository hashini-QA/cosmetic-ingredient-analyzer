import json
import os
from openai import OpenAI

# Initialize client (uses OPENAI_API_KEY from env)
client = OpenAI()

SYSTEM_PROMPT = """
You are a cosmetic chemistry assistant.
Your task is to extract and normalize cosmetic ingredient names.

Rules:
- Return ONLY valid INCI ingredient names
- Remove percentages, numbers, marketing words
- Convert synonyms to standard names (e.g. aqua → water)
- Lowercase everything
- Do NOT explain anything
- Return STRICT JSON only
"""

def llm_normalize_ingredients(raw_text: str) -> list[str]:
    if not raw_text or len(raw_text.strip()) < 10:
        return []

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Normalize the following ingredient text into JSON.

Text:
\"\"\"{raw_text}\"\"\"

Output format:
{{
  "ingredients": ["ingredient1", "ingredient2"]
}}
"""
            }
        ],
        temperature=0.0
    )

    content = response.choices[0].message.content.strip()

    try:
        data = json.loads(content)
        ingredients = data.get("ingredients", [])
        return [i.strip().lower() for i in ingredients if isinstance(i, str)]
    except Exception:
        # Fail safe
        return []
