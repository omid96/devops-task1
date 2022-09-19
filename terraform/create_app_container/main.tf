resource "docker_image" "app" {
  name = "${var.repo_address}/task1"
}

resource "docker_container" "app" {
  name  = "task1"
  image = docker_image.app.name
  ports {
    internal = 8000
    external = 80
  }
}
