import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
model="gemini-2.5-flash",
contents=os.environ["USER_PROMPT"]
)

terraform_code = response.text

file_content = terraform_code.replace("`terraform", "")
file_content = file_content.replace("`hcl", "")
file_content = file_content.replace("```", "")

os.makedirs("terraform", exist_ok=True)

open("terraform/main.tf", "w").write(file_content)

print(file_content)
