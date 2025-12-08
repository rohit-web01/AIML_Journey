class Laptop : 
    storage_type = "SSD"

    def __init__(self, RAM, storage) :
        self.RAM = RAM
        self.storage = storage

    # instance method
    def get_info(self) :
        print(f"Laptop has {self.RAM} & {self.storage} {self.storage_type}")


l1 = Laptop("8gb", "256gb")
l2 = Laptop("16gb", "512gb")

l1.get_info()
l2.get_info()