import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
prompt = os.environ.get("USER_PROMPT")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
model="gemini-2.5-flash",
contents=f"""
Generate valid Terraform HCL only.

Rules:

* Output only Terraform code
* No markdown
* No explanations
* No triple backticks

Request:
{prompt}
"""
)

terraform_code = response.text.strip()

terraform_code = terraform_code.replace("`terraform", "")
terraform_code = terraform_code.replace("`hcl", "")
terraform_code = terraform_code.replace("```", "")

os.makedirs("terraform", exist_ok=True)

with open("terraform/main.tf", "w", encoding="utf-8") as f:
f.write(terraform_code)

print("===== GENERATED TERRAFORM =====")
print(terraform_code)
print("================================")
