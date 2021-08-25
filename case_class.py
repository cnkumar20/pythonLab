from dataclasses import dataclass

@dataclass
class CustomerOrder:
  order_id: int
  customer_id: str
  item_name: str

order = CustomerOrder(1, '001', 'Guitar')
print(order)
