from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, JSON, ForeignKey, Boolean

from api.auth.auth_models import user

metadata = MetaData()


question = Table(
    "question",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("question_title", String(length=200), nullable=False),
    Column("choices", JSON, nullable=False),
    Column("answer", String(length=25), nullable=False),
    Column("reference", String(length=100), nullable=False),
    Column("reference_link", String(length=200), nullable=True),
    Column("added_by", ForeignKey(user.c.id), nullable=False),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("section_id", Integer, ForeignKey("section.id"), nullable=False),
    Column("active", Boolean, default=False, nullable=False)
)