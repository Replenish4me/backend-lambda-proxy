data "aws_route53_zone" "root_domain" {
  name         = "caioruiz.com"
  private_zone = false
}

data "aws_acm_certificate" "cert" {
  domain   = "*.api.replenish4me.caioruiz.com"
  statuses = ["ISSUED"]
}

# The domain name to use with api-gateway
resource "aws_api_gateway_domain_name" "domain_name" {
  domain_name = "${var.env}.api.replenish4me.caioruiz.com"

  certificate_arn = "${data.aws_acm_certificate.cert.arn}"
}

resource "aws_route53_record" "sub_domain" {
  name    = "${var.env}.api.replenish4me.caioruiz.com"
  type    = "A"
  zone_id = "${data.aws_route53_zone.root_domain.zone_id}"

  alias {
    name                   = "${aws_api_gateway_domain_name.domain_name.cloudfront_domain_name}"
    zone_id                = "${aws_api_gateway_domain_name.domain_name.cloudfront_zone_id}"
    evaluate_target_health = false
  }
}

# Create api mapping

resource "aws_api_gateway_base_path_mapping" "mapping" {
  depends_on = [ aws_api_gateway_deployment.deployment ]
  domain_name = "${aws_api_gateway_domain_name.domain_name.id}"
  api_id = "${aws_api_gateway_rest_api.api.id}"
  stage_name  = "${var.env}"
  base_path = ""
}
