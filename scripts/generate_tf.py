import os
from google import genai

# Create Gemini client

client = genai.Client(
api_key=os.environ["GEMINI_API_KEY"]
)

# Get prompt from GitHub Actions

prompt = os.environ["USER_PROMPT"]

# Generate Terraform

response = client.models.generate_content(
model="gemini-2.5-flash",
contents=f"""
Generate valid Terraform HCL code only.

Requirements:

* Return ONLY Terraform code
* No markdown
* No triple backticks
* No explanations
* Include AWS provider block when required

User Request:
{prompt}
"""
)

terraform_code = response.text

# Remove markdown if model accidentally returns it

terraform_code = terraform_code.replace("`terraform", "")
terraform_code = terraform_code.replace("`hcl", "")
terraform_code = terraform_code.replace("```", "")
terraform_code = terraform_code.strip()

# Create terraform directory if it doesn't exist

os.makedirs("terraform", exist_ok=True)

# Write Terraform code to file

with open("terraform/main.tf", "w", encoding="utf-8") as f:
f.write(terraform_code)

print("===== GENERATED TERRAFORM =====")
print(terraform_code)
print("================================")
print("Terraform file generated successfully")
