#!/usr/bin/python3
"""
Module for MyList class
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
EOFcd /alu-higher_level_programming/python-inheritance

cat <<EOF > 1-my_list.py
#!/usr/bin/python3
"""
Module for MyList class
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
