resource "docker_tag" "task1" {
  source_image = "task1"
  target_image = "node004:5001/task1"
}

resource "docker_registry_image" "task1" {
  name                 = "node004:5001/task1"
  insecure_skip_verify = true

  build {
    context    = "../../"
    dockerfile = "../../Dockerfile"
  }
}
