import os

prompt = os.environ["USER_PROMPT"].lower()

terraform_code = ""

if "s3" in prompt and "bucket" in prompt:

```
bucket_name = "ai-demo-bucket"

words = prompt.replace(",", " ").split()

for word in words:
    if "bucket" in word:
        continue

terraform_code = f'''
```

terraform {{
required_providers {{
aws = {{
source  = "hashicorp/aws"
version = "~> 5.0"
}}
}}
}}

provider "aws" {{
region = "us-east-1"
}}

resource "aws_s3_bucket" "demo" {{
bucket = "{bucket_name}"
}}
'''

elif "ec2" in prompt or "instance" in prompt:

```
terraform_code = '''
```

terraform {
required_providers {
aws = {
source  = "hashicorp/aws"
version = "~> 5.0"
}
}
}

provider "aws" {
region = "us-east-1"
}

resource "aws_instance" "demo" {
ami           = "ami-0c02fb55956c7d316"
instance_type = "t2.micro"
}
'''

else:
raise Exception(
f"Unsupported request: {prompt}. Try S3 bucket or EC2 instance."
)

os.makedirs("terraform", exist_ok=True)

with open("terraform/main.tf", "w", encoding="utf-8") as f:
f.write(terraform_code)

print(terraform_code)
