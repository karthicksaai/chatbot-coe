import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

async def populate_qa_pairs():
    # Connect to MongoDB
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db = client[os.getenv("DB_NAME")]
    
    # Initial Q&A pairs
    qa_pairs = [
        {
            "question": "how to apply for revaluation",
            "answer": "To apply for revaluation: 1) Log in to student portal 2) Select the subject 3) Pay the fees 4) Submit application within 7 days of result declaration.",
            "source": "manual",
            "created_at": datetime.now()
        },
        {
            "question": "exam schedule",
            "answer": "You can check the examination schedule on the student portal or notice board. For specific dates, please provide your course and semester.",
            "source": "manual",
            "created_at": datetime.now()
        },
        {
            "question": "result",
            "answer": "Results are published on the university website and student portal. You can also check the notice board or contact your department.",
            "source": "manual",
            "created_at": datetime.now()
        },
        {
            "question": "fee payment",
            "answer": "Examination fees can be paid online through the student portal or at the bank counter. The last date for regular fee payment is typically 2 weeks before exams.",
            "source": "manual",
            "created_at": datetime.now()
        }
    ]
    
    # Create collection if it doesn't exist
    if "qa_pairs" not in await db.list_collection_names():
        await db.create_collection("qa_pairs")
    
    # Insert Q&A pairs
    result = await db.qa_pairs.insert_many(qa_pairs)
    print(f"Inserted {len(result.inserted_ids)} Q&A pairs into the database.")
    
    # Close connection
    client.close()

if __name__ == "__main__":
    asyncio.run(populate_qa_pairs())
