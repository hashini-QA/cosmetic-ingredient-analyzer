import requests

BASE_SEARCH_URL = "https://world.openbeautyfacts.org/cgi/search.pl"

def search_products_by_name(product_name: str, page_size: int = 10) -> list[dict]:
    """
    Returns a list of products with minimal fields:
    product_name, brands, code (barcode), ingredients_text
    """
    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": page_size,
    }

    resp = requests.get(BASE_SEARCH_URL, params=params, timeout=20)
    resp.raise_for_status()
    data = resp.json()

    products = []
    for p in data.get("products", []):
        products.append({
            "product_name": p.get("product_name") or "Unknown product",
            "brand": p.get("brands") or "Unknown brand",
            "barcode": p.get("code"),
            "ingredients_text": p.get("ingredients_text") or "",
        })

    # Remove entries with no useful name
    products = [p for p in products if p["product_name"] != "Unknown product"]
    return products
