variable "project_name" {
  description = "Project name used for resource naming and tags."
  type        = string
  default     = "eks-hpa-vpa-poc"
}

variable "environment" {
  description = "Deployment environment used for resource naming and tags."
  type        = string
  default     = "dev"
}

variable "aws_region" {
  description = "AWS region for the project."
  type        = string
  default     = "us-east-1"
}
