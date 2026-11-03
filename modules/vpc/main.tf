resource "null_resource" "vpc" {
  triggers = {
    name = var.name
  }
}
