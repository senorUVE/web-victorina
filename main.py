from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, select
from databases import Database
import requests
from datetime import datetime

DATABASE_URL = "postgresql://user:password@localhost/trivia_db"

metadata = MetaData()

trivia_table = Table(
    "trivia",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("question_id", Integer),
    Column("question_text", String),
    Column("answer_text", String),
    Column("creation_date", DateTime)
)

app = FastAPI()
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class QuestionInput(BaseModel):
    questions_num: int


@app.post("/")
async def get_question(data: QuestionInput):
    for _ in range(data.questions_num):
        response = requests.get("https://jservice.io/api/random?count=1").json()[0]
        
        question_exists = await database.fetch_one(
            select([trivia_table]).where(trivia_table.c.question_id == response['id'])
        )
        
        while question_exists:
            response = requests.get("https://jservice.io/api/random?count=1").json()[0]
            question_exists = await database.fetch_one(
                select([trivia_table]).where(trivia_table.c.question_id == response['id'])
            )
        
        query = trivia_table.insert().values(
            question_id=response['id'],
            question_text=response['question'],
            answer_text=response['answer'],
            creation_date=datetime.strptime(response['airdate'], "%Y-%m-%d")
        )
        await database.execute(query)

    last_question = await database.fetch_one(
        select([trivia_table]).order_by(trivia_table.c.id.desc())
    )
    if not last_question:
        return {}
    return {"question": last_question["question_text"], "answer": last_question["answer_text"]}

