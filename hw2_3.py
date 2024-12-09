class Computer:
    def __init__(self, brand, model, memory):
        self.brand = brand
        self.model = model
        self.memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f"Computer(Brand: {self.brand}, Model: {self.model}, Memory: {self.memory}GB)"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"Phone(Brand: {self.brand}, Model: {self.model}, Phone Number: {self.phone_number})"


class SmartPhone(Computer, Phone):
    def __init__(self, brand, model, memory, phone_number):
        Computer.__init__(self, brand, model, memory)
        Phone.__init__(self, brand, model, phone_number)

    def use_gps(self, location):
        print(f"Simulating route to {location}...")

    def __str__(self):
        return f"SmartPhone(Brand: {self.brand}, Model: {self.model}, Memory: {self.memory}GB, Phone Number: {self.phone_number})"


if __name__ == "__main__":
    smartphone = SmartPhone("Apple", "iPhone 14", 128, "+123456789")
    print(smartphone)
    smartphone.use_gps("Central Park")

    computer1 = Computer("Dell", "XPS 13", 16)
    computer2 = Computer("HP", "Spectre x360", 32)

    print(computer1)
    print(computer2)

    print(computer1 == computer2)  # False
    print(computer1 < computer2)   # True