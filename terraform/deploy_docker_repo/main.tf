resource "docker_image" "local_registry" {
  name = "registry:2"
}

resource "docker_container" "local_registry" {
  name  = "registry"
  image = docker_image.local_registry.name
  env   = ["REGISTRY_HTTP_ADDR=0.0.0.0:5001"]
  ports {
    internal = 5001
    external = 5001
  }
}
