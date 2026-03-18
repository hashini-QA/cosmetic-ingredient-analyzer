from openai import OpenAI

client = OpenAI()

def chatbot_answer(messages, analysis, skin_type):
    """
    messages: full chat history (list of dicts)
    analysis: output from analyze_ingredients
    skin_type: selected skin type
    """

    system_prompt = f"""
    You are a skincare assistant.

    Skin Type: {skin_type}
    Safety Score: {analysis['summary']['safety_score']}
    Average Comedogenic Score: {analysis['summary']['avg_comedogenic']}

    Flagged Ingredients:
    {analysis['summary']['flagged_items']}

    Ingredient Details:
    {analysis['details']}

    Answer clearly and simply.
    """

    full_messages = [{"role": "system", "content": system_prompt}] + messages

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=full_messages
    )

    return response.choices[0].message.content
