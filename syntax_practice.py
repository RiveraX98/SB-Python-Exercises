def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c"
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """


   
   
    if unit_in == "f":
        converted_temp = (temp- 32) * 5 / 9
        print (unit_out,"=", converted_temp)
    if unit_in == "c":
        converted_temp = (temp * 9/5) + 32
        print(unit_out,"=",converted_temp)
    elif unit_in != "f" and unit_in != "c":
        print(f"Invalid unit {unit_in}")
    elif unit_out != "f" or unit_out != "c":
        print(f"Invalid unit {unit_out}")
   



""""
print("c", "f", 0, convert_temp("z", "f", 32), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
"""




def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    nums_in_range = [num for num in nums if num>= lowest and num <= highest]
    print (nums_in_range)
    # YOUR CODE HERE


# in_range([10, 20, 30, 40, 50], 15, 30)












def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    if 7 in nums:
        print("true")
    else:
        print("false")
  

# print("should be true", any7([1, 2, 7, 4, 5]))
# print("should be false", any7([1, 2, 4, 5]))














def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    nums = range (start, stop +1)
    for n in nums:
        print(n)




def print_upper_words(words,start_with):
      
    new_words = [word.upper() for word in words if word[0] in start_with]
    for words in new_words:
        print(words)
    
    














def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    total = 0
    for num in nums:
        total = num + total
    return total 

    
        


# print("sum_nums returned", sum_nums([1, 2, 3, 4]))

