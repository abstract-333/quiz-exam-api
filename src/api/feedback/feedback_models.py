from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.mysql import SMALLINT

from api.auth.auth_models import user
from api.question.question_models import question

metadata = MetaData()

feedback = Table(
    "feedback",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rating", SMALLINT(unsigned=True), nullable=False),
    Column("feedback_title", String(length=255), nullable=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id), nullable=False),
    Column("question_id", Integer, ForeignKey(question.c.id), nullable=False),
    Column("question_author_id", Integer, ForeignKey(user.c.id), nullable=False)
)
