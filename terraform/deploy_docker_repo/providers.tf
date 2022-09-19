provider "docker" {
  host     = "ssh://ubuntu@node004"
  ssh_opts = ["-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null"]
}
