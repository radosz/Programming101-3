from CashDesk import Bill, BillBatch, CashDesk

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

print(desk.take_money(batch))
print(desk.take_money(Bill(10)))

print(desk.total())  # 390
print(desk.inspect())
