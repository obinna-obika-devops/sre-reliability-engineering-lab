terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "backup_vault_name" {
  type    = string
  default = "sre-reliability-lab"
}

resource "aws_backup_vault" "this" {
  name = var.backup_vault_name
}

resource "aws_cloudwatch_log_group" "application" {
  name              = "/sre/reliability-lab/application"
  retention_in_days = 14
}

output "backup_vault_arn" {
  value = aws_backup_vault.this.arn
}
