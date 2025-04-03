# import os
# import google.generativeai as genai
# from ..config.database import get_database
# from dotenv import load_dotenv

# load_dotenv()

# # Configure Gemini API
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)

# class ChatService:
#     @staticmethod
#     async def process_message(message: str) -> str:
#         # Get database connection
#         db = await get_database()
        
#         # Convert message to lowercase for case-insensitive matching
#         query = message.lower()
        
#         # Check if we have a predefined answer in MongoDB
#         result = await db.qa_pairs.find_one({"question": {"$regex": query, "$options": "i"}})
        
#         if result:
#             # Return predefined answer from database
#             return result["answer"]
#         else:
#             # Use Gemini for unknown questions
#             try:
#                 # Initialize the Gemini model
#                 model = genai.GenerativeModel(model_name='gemini-1.5-flash')
                
#                 # Add context about being a COE assistant
#                 prompt = f"""You are a Controller of Examinations (COE) assistant for a college. 
#                 Answer the following student query professionally and concisely:
#                 {message}"""
                
#                 # Generate content based on the input text
#                 response = model.generate_content(prompt)
                
#                 # Store the new Q&A pair in the database for future use
#                 await db.qa_pairs.insert_one({
#                     "question": message,
#                     "answer": response.text,
#                     "source": "gemini",
#                     "created_at": datetime.now()
#                 })
                
#                 return response.text
#             except Exception as e:
#                 return f"I'm sorry, I couldn't process your request at the moment. Error: {str(e)}"


import os
import google.generativeai as genai
from datetime import datetime
from ..config.database import get_database
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

class ChatService:
    @staticmethod
    async def process_message(message: str) -> str:
        # Get the database connection
        db = await get_database()
        
        # Lowercase user input to ensure case-insensitive comparison
        query = message.lower()
        result = None
        
        # Retrieve all QA pairs (assuming a small collection)
        qa_pairs = await db.qa_pairs.find().to_list(length=100)
        
        # Check if any predefined question (keyword) is part of the user query
        for qa in qa_pairs:
            stored_keyword = qa["question"].lower()
            if stored_keyword in query:
                result = qa
                break
        
        if result:
            return result["answer"]
        else:
            # No predefined answer found; use Gemini for AI-generated response
            try:
                model = genai.GenerativeModel(model_name='gemini-1.5-flash')
                prompt = (
                    "You are a Controller of Examinations (COE) assistant for a college. "
                    "Answer the following student query professionally and concisely:\n"
                    f"{message}"
                )
                response = model.generate_content(prompt)
                
                # Optionally store the newly generated Q&A pair for future reference
                await db.qa_pairs.insert_one({
                    "question": message,
                    "answer": response.text,
                    "source": "gemini",
                    "created_at": datetime.now()
                })
                return response.text
            except Exception as e:
                return f"I'm sorry, I couldn't process your request at the moment. Error: {str(e)}"
