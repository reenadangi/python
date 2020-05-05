def maximum69Number (num):
        """
        :type num: int
        :rtype: int
        """
        return str(num).replace('6','9',1)
print(maximum69Number(9669))