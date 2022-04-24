from sqlalchemy import Table, Text, Integer, VARCHAR, MetaData, Column, JSON

meta = MetaData()
post = Table(
    "post",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", VARCHAR, nullable=True),
    Column(
        "body",
        Text,
    ),
    Column("jsonb_field", JSON),
)
