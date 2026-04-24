from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import mysql.connector
import os

app = FastAPI()


MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DB   = os.getenv("MONGO_INITDB_DATABASE")
MONGO_HOST = os.getenv("MONGO_HOST", "db_mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"
mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client[MONGO_DB]

def get_mysql_conn():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db_mysql"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.get("/posts")
async def get_posts():
    cursor = mongo_db.posts.find({}, {"_id": 0})
    posts = await cursor.to_list(length=100)
    return posts

@app.get("/users")
def get_users():
    conn = get_mysql_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utilisateurs")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
