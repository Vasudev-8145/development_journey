
from google import genai

from mysql import connector

connection = connector.connect(
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "hospital_register_db"
    )

cursor = connection.cursor()

query = "select * from patient_list where id=1"
cursor.execute(query)
patient = cursor.fetchone()

GEMINI_API_KEY = 5
client = genai.Client(api_key=GEMINI_API_KEY)

prompt = f"""
You are a patient register analysis system.

Analyze the following patient register.

Customer Name:
{patient[1]}

appoinment_status:
{patient[3]}

treatment_status:
{patient[4]}

Provide the following information:

1. Priority
2. Sentiment
3. Summary
4. Suggested response

Priority must be one of:

low
medium
high
urgent

Sentiment must be one of:

positive
neutral
negative

Return the answer in a clear format.
"""



response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
    )

print(response)