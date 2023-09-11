
def main():
    cookie_jar = Jar()

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return(f"There are {self.size} cookies in the jar.")

    def deposit(self, n):
        if n <= self.capacity:
            self._size += n
        else:
            raise ValueError("There isnt enough room in the jar")

    def withdraw(self, n):
        if self.size > n:
            self._size -= n


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, n):
        if n < 1:
            raise ValueError("Please provide a number greater than 0")
        self._capacity = n

    @property
    def size(self):
        return self._size




if __name__ == "__main__":
    main()