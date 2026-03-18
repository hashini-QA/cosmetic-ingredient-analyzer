from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), index=True)
    skin_type = Column(String(50))
    product_name = Column(String(255))
    brand = Column(String(255))

    # store raw + normalized ingredients as text (JSON-like string)
    raw_ingredients_text = Column(Text)
    normalized_ingredients = Column(Text)

    safety_score = Column(Integer)
    flagged_ingredients = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
