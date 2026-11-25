module "vpc" {
  source = "../modules/vpc"

  name = "sandbox-related-v3"
}

module "storage" {
  source = "../modules/storage"

  bucket_name = "sandbox-uploads"
}
