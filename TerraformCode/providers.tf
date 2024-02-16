terraform {
  required_version = ">=0.12"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.0"
    }
  }

  backend "azurerm" {
    resource_group_name   = "demoplatform"
    storage_account_name  = "blobdemoplatform"
    container_name        = "test"
    key                   = "ttJm+Iz0XpwiRnaVILVup+7KmXJZd9+UkLsI0sLKawyFOSZCepOeNoAytD1d6dE9REvIRjktSwLk+AStjmV3pg=="
  }
  
}

