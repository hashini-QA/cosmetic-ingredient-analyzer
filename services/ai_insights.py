import json
from openai import OpenAI

client = OpenAI()

def generate_ai_insights(product, skin_type, analysis):
    prompt = f"""
Product: {product}
Skin type: {skin_type}

Ingredient details:
{json.dumps(analysis["details"], indent=2)}  

Explain:
- What this product does
- Comedogenic impact
- Who should use it
- Any cautions
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
