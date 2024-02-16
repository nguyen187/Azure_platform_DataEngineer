output "db_name_out"{
    value = azurerm_mssql_database.example.name
}
output "server_name_out"{
    value = azurerm_sql_server.example.name
}