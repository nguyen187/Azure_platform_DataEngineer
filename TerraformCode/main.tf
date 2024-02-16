# Import providers from providers.tf
provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

module "resource_group" {
  source               = "./resource_group"
  resource_group_name  = "my-resource-group187201"
  location             = "East US"
}

module "storage_account" {
  source                = "./storage_account"
  storage_account_name  = "mystorageaccount187201"
  resource_group_name   = module.resource_group.rg_name_out
  location              = "East US"
}

module "virtual_machine" {
  source                = "./virtual_machine"
  vm_name               = "vps_example187201"
  vm_size               = "Standard_DS2_v2"
  admin_username        = "adminuser"
  admin_password        = "Password12345!"
  resource_group_name   = module.resource_group.rg_name_out
  location              = module.resource_group.rg_location_out
}


module "data_warehouse" {
  source                = "./data_warehouse"
  sql_server_name       = "my-sql-server187201"
  sql_database_name     = "my-sql-database187201"
  administrator_login   = "adminuser"
  administrator_login_password = "Password12345!"
  resource_group_name   = module.resource_group.rg_name_out
  location              = module.resource_group.rg_location_out
}




