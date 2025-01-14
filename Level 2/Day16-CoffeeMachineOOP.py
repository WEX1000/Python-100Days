import prettytable
table1 = ["First", "Second", "Third"]
table = prettytable.PrettyTable()
table.add_column("FirstColumn", table1)
table.add_column("SecondColumn", table1)
table.align = "l"
print(table)