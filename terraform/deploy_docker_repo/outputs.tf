output "registry_address" {
  value = "${var.hostname}:${docker_container.local_registry.ports[0].external}"
}
