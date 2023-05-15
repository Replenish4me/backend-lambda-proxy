resource "aws_lambda_function" "my_function" {
  filename      = "../app.zip"
  function_name = "${var.function_name}-${var.env}"
  role          = aws_iam_role.my_role.arn
  handler       = "app.handler.lambda_handler"
  runtime       = "python3.9"

  source_code_hash = filebase64sha256("../app.zip")

  lifecycle {
    create_before_destroy = true
  }

  environment {
    variables = {
      env = var.env
    }
  }
}

resource "aws_iam_role" "my_role" {
  name = "my-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "my_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.my_role.name
}
