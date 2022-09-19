output "published_port" {
  value = docker_container.app.ports[0].external
}
