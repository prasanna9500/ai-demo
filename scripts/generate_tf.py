import os
from google import genai

client = genai.Client(
api_key=os.environ["GEMINI_API_KEY"]
)

prompt = os.environ["USER_PROMPT"]

response = client.models.generate_content(
model="gemini-2.5-flash",
contents=f"""
Generate valid Terraform HCL code only.

Rules:

* Return ONLY Terraform code
* Do NOT use markdown
* Do NOT use triple backticks
* Do NOT provide explanations
* Include provider configuration if required

User Request:
{prompt}
"""
)

terraform_code = response.text

# Remove markdown formatting if present

terraform_code = terraform_code.replace("`terraform", "")
terraform_code = terraform_code.replace("`hcl", "")
terraform_code = terraform_code.replace("```", "")
terraform_code = terraform_code.strip()

os.makedirs("terraform", exist_ok=True)

with open("terraform/main.tf", "w") as f:
f.write(terraform_code)

print("===== GENERATED TERRAFORM =====")
print(terraform_code)
print("================================")
print("Terraform file generated successfully")
