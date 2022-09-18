resource "maas_instance" "t2_micro" {
  count                = 1
  hostname             = var.hostname
  release_erase_quick  = true
  release_erase_secure = false
}
