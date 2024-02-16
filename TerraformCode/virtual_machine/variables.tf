variable "vm_name" {
  type    = string
  description = "Name of the Azure Virtual Machine"
}

variable "vm_size" {
  type    = string
  description = "Size of virtual machine"
}

variable "admin_username" {
  type    = string
  description = "Name of the admin user"
}

variable "admin_password" {
  type    = string
  description = "Password for admin "
}
variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
}

variable "location" {
  description = "Azure region for the Resource Group"
  type        = string
}
