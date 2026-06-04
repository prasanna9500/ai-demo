import os
import google.generativeai as genai

# Read Gemini API Key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Read prompt from GitHub workflow
prompt = os.getenv("USER_PROMPT")

# Ask Gemini to generate Terraform
response = model.generate_content(
    f"""
Generate Terraform code only.

Request:
{prompt}

Output only Terraform HCL code.
"""
)

# Create terraform folder if needed
os.makedirs("terraform", exist_ok=True)

# Save Terraform code
with open("terraform/main.tf", "w") as f:
    f.write(response.text)

print("Terraform file generated")
