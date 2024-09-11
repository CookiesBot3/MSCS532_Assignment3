class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize a list of empty lists (chains)

    def hash_function(self, key):
        # Simple hash function: modulo operation to get an index within the table size
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        hash_key = self.hash_function(key)
        # Check if the key already exists, if so, update the value
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)  # Update existing key-value pair
                return
        # If key does not exist, append the new key-value pair
        self.table[hash_key].append((key, value))

    def search(self, key):
        # Search for a value by its key
        hash_key = self.hash_function(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v  # Return value if found
        return None  # Key not found

    def delete(self, key):
        # Delete a key-value pair by its key
        hash_key = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]  # Remove the key-value pair
                return True  # Return True to indicate successful deletion
        return False  # Key not found

    def display(self):
        # Helper function to display the contents of the hash table
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


# Example Usage
hash_table = HashTable(10)  # Create a hash table of size 10

hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("grape", 30)
hash_table.insert("orange", 40)
hash_table.insert("peach", 50)  # Likely to collide with "apple"
hash_table.insert("cherry", 60)  # Likely to collide with "banana"
hash_table.insert("mango", 44)

# Display the hash table
hash_table.display()

# Search for keys
print("Search 'apple':", hash_table.search("apple"))
print("Search 'banana':", hash_table.search("banana"))
print("Search 'pear':", hash_table.search("pear"))  # Key not found

# Delete a key
print("Delete 'grape':", hash_table.delete("grape"))
print("Delete 'pear':", hash_table.delete("pear"))  # Key not found

# Display the hash table
hash_table.display()