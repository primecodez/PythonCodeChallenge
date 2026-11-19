#python APIFETCHER.py
import os
from dotenv import load_dotenv
from google import genai

# 1. Load the variables from the .env file into your system
load_dotenv() 

# 2. Retrieve the key securely
my_api_key = os.environ.get("GEMINI_API_KEY")

# 3. Initialize the client using the variable
client = genai.Client(api_key=my_api_key)

# 4. The text you want to convert into numbers
text_to_embed = "Python is great for backend engineering."

# 5. Call the Gemini embedding model
response = client.models.embed_content(
    model='gemini-embedding-2',
    contents=text_to_embed,
)
# 6. Extract the vector array from the response
vector_array = response.embeddings[0].values

# 7. Print the results
print(f"Original Text: '{text_to_embed}'\n")
print(f"Total numbers in the vector: {len(vector_array)}")
print(f"First 5 numbers of the embedding: {vector_array[:5]}")