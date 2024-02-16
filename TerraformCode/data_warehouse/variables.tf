variable "sql_server_name" {
  description = "Name of the Azure SQL Server"
  type        = string
}

variable "sql_database_name" {
  description = "Name of the Azure SQL Database"
  type        = string
}

variable "administrator_login" {
  description = "Administrator login for SQL Server"
  type        = string
}

variable "administrator_login_password" {
  description = "Administrator login password for SQL Server"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
}

variable "location" {
  description = "Azure region for the Data Warehouse"
  type        = string
}

