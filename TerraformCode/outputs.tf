output "resource_group_name" {
  value = module.resource_group.rg_name_out
}
output "vm_name" {
  value = module.virtual_machine.vm_name_out
}

output "storage_account_name" {
  value = module.storage_account.st_name_out
}

output "sql_server_name" {
  value = module.data_warehouse.server_name_out
}

output "sql_database_name" {
  value = module.data_warehouse.db_name_out
}
