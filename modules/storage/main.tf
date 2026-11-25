resource "aws_s3_bucket" "uploads" {
  bucket = var.bucket_name
  acl    = "public-read"
}

resource "aws_security_group" "bastion" {
  name = "${var.bucket_name}-bastion"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
