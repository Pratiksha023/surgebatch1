resource "azurerm_resource_group" "example2" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    environment = var.environment
  }
}