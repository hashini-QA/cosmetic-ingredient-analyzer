from sqlalchemy import text
from db.mysql_db import engine

def create_user(name, email):
    with engine.begin() as conn:
        result = conn.execute(
            text("""
                INSERT INTO users (name, email)
                VALUES (:name, :email)
            """),
            {"name": name, "email": email}
        )
        return result.lastrowid


def save_search(user_id, ingredients, safety_score, avg_comed):
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO searches
                (user_id, ingredients, safety_score, avg_comedogenic)
                VALUES (:user_id, :ingredients, :safety_score, :avg_comed)
            """),
            {
                "user_id": user_id,
                "ingredients": ingredients,
                "safety_score": safety_score,
                "avg_comed": avg_comed
            }
        )
