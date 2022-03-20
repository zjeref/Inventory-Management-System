
from Schema.orderSchema import Order
from Schema.customerSchema import Customer
from Schema.ItemSchema import Items

from models.ItemModel import ItemsModel
from models.orderModel import OrderModel
from models.customerModel import CustomerModel



class main():
    def __init__(self):
        self.itemModel = ItemsModel()
        self.orderModel = OrderModel()
        self.customerModel = CustomerModel()

        item1 = ["1001","customer1","description","10","100"]
        self.itemModel.insert_items(item1)

        print(self.itemModel.getAllItems())    


main()