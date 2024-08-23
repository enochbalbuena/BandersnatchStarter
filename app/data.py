from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

load_dotenv()


class Database:
    def __init__(self):
        self.client = MongoClient(getenv("DB_URL"), tlsCAFile=where())
        self.db = self.client["MonsterDatabase"]
        self.collection = self.db["Monsters"]

    def seed(self, amount: int):
        """Seed the database with a specified number of Monster documents."""
        monsters = []
        for _ in range(amount):
            monster = Monster().to_dict()
            monsters.append(monster)

        self.collection.insert_many(monsters)

    def reset(self):
        """Delete all documents from the collection."""
        self.collection.delete_many({})

    def count(self) -> int:
        """Return the number of documents in the collection."""
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """Return a DataFrame containing all documents in the collection."""
        data = list(self.collection.find({}, {'_id': False}))
        return DataFrame(data)

    def html_table(self) -> str:
        """Return an HTML table representation of the DataFrame, or None if the collection is empty."""
        df = self.dataframe()
        if df.empty:
            return 'None'
        return df.to_html(index=False)
