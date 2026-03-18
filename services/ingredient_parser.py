import re

_SPLIT_REGEX = re.compile(r"[,\n;•|]+")

def clean_ingredient_token(token: str) -> str:
    token = token.strip().lower()
    # remove bracket content like (10%) or [blah]
    token = re.sub(r"\(.*?\)", "", token)
    token = re.sub(r"\[.*?\]", "", token)
    # remove percentages and extra symbols
    token = re.sub(r"\d+(\.\d+)?\s*%","", token)
    token = re.sub(r"[^a-z0-9\s\-\/]", " ", token)
    token = re.sub(r"\s+", " ", token).strip()
    return token

def parse_ingredients_text(raw_text: str) -> list[str]:
    if not raw_text:
        return []

    # Some API strings contain "Ingredients:" prefix
    raw_text = raw_text.replace("ingredients:", "").replace("ingredient:", "")
    parts = _SPLIT_REGEX.split(raw_text)

    cleaned = []
    for p in parts:
        c = clean_ingredient_token(p)
        if c and len(c) > 1:
            cleaned.append(c)

    # de-duplicate while keeping order
    seen = set()
    out = []
    for x in cleaned:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

from services.llm_normalizer import llm_normalize_ingredients

def smart_parse_ingredients(raw_text: str) -> list[str]:
    """
    Try rule-based parsing first.
    If output looks poor, fallback to LLM.
    """
    rule_based = parse_ingredients_text(raw_text)

    # Heuristics to decide if LLM is needed
    needs_llm = (
        len(rule_based) < 3 or
        any(len(x) > 40 for x in rule_based) or
        any("extract" in x or "contains" in x for x in rule_based)
    )

    if needs_llm:
        llm_result = llm_normalize_ingredients(raw_text)
        return llm_result if llm_result else rule_based

    return rule_based
