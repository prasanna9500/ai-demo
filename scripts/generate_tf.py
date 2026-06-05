import os

prompt = os.environ["USER_PROMPT"].lower()

if "s3" in prompt:
    terraform_code = """
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "ai-demo-tf-state-89312"
    key    = "terraform/demo.tfstate"
    region = "us-east-1"
  }

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

resource "aws_s3_bucket" "demo" {
  bucket = "demo-bucket-89312"
}
"""

elif "ec2" in prompt or "instance" in prompt:
    terraform_code = """
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "ai-demo-tf-state-89312"
    key    = "terraform/demo.tfstate"
    region = "us-east-1"
  }

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

  tags = {
    Name = "AI-Demo-Instance"
  }
}
"""

else:
    raise Exception(f"Unsupported request: {prompt}")

os.makedirs("terraform", exist_ok=True)

with open("terraform/main.tf", "w", encoding="utf-8") as f:
    f.write(terraform_code)

print(terraform_code)
