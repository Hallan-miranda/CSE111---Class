def main():
  # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
  
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")

    fruit_list.append("Orange")
    print(f"Append: {fruit_list}")

    apple_index = fruit_list.index("apple")
    fruit_list.insert((apple_index + 1), "cherry")
    print(f"Insert: {fruit_list}")

    banana_index = fruit_list.index("banana")
    fruit_list.pop(banana_index)
    print(f"pop: {fruit_list}")

    removed = fruit_list.pop(-1)
    print(f"Removed: {removed   }")

    fruit_list.sort()
    print(f"sort: {fruit_list}")

    fruit_list.clear()
    print(f"clear: {fruit_list}")


main()

    