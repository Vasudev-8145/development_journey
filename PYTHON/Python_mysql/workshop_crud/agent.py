

from google import genai

from mysql import connector

connection = connector.connect(
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "auto_service_db"
    )

cursor = connection.cursor()

query = "select * from job_cards where id=1"
cursor.execute(query)
job = cursor.fetchone()


GEMINI_API_KEY = 5
client = genai.Client(api_key=GEMINI_API_KEY)

prompt = f"""
You are a automobile job card analysis system.

Analyze the following dob card.

Customer Name:
{job[1]}

description:
{job[4]}

status:
{job[6]}

Provide the following information:

1. Category
2. Priority
3. Sentiment
4. Summary
5. Suggested response

Category must be one of:

payment
delivery
account
technical
refund
other

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