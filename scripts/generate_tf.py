import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = os.environ["USER_PROMPT"]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Generate Terraform code only.

Request:
{prompt}

Output only Terraform HCL code.
"""
)

os.makedirs("terraform", exist_ok=True)

with open("terraform/main.tf", "w") as f:
    f.write(response.text)

print("Terraform file generated successfully")
