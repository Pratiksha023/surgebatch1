provider "azurerm" {
    features {}
}

# resource "azurerm_resource_group" "example" {
#   name     = "jatinbhalla"
#   location = "eastus"
#   tags = {
#     environment = "dev"
#   }
# }

resource "azurerm_resource_group" "example2" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    environment = var.environment
  }
}

resource "azurerm_storage_account" "example" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.example2.name
  location                 = azurerm_resource_group.example2.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}