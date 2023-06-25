def product(a, b):
    # Return product of a and b.
    total = (a+b)
    return total


def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'
    """
    match day_of_week:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wenesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saterday"
        case _:
            return "Invalid Weekday"


def last_element(lst):
    # Return last item in list (None if list is empty.
    last_idx = len(lst) - 1
    print(lst[last_idx])


def number_compare(a, b):
    # Report on whether a>b, b>a, or b==a

    if a > b:
        print('First is greater')
    elif b > a:
        print('Second is greater')
    else:
        print("Numbers are equal")


def reverse_string(phrase):
    # reverse string
    word_list = list(phrase)
    word_list.reverse()
    return "".join(word_list)


def single_letter_count(word, letter):
    # How many times does letter appear in word (case-insensitively)?
    return word.count(letter)


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.
        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = {}
    for ltr in phrase:
        count[ltr] = phrase.count(ltr)
    print(count)


def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add
    """
    if command == "remove":
        if location == 'beginning':
            lst.pop(0)
        elif location == "end":
            last_idx = len(lst) - 1
            lst.pop(last_idx)
        else:
            print("Not valid Location")
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
        elif location == "end":
            lst.append(value)
        else:
            print("Not valid Location")
    else:
        print("Not Valid Command")


def is_palindrome(phrase):
    # Is phrase a palindrome?
    word_list = list(phrase.lower())
    word_list.reverse()
    reversed = "".join(word_list)
    if phrase.lower() == reversed:
        print("True")
    else:
        print("False")


def frequency(lst, search_term):
    """Return frequency of term in lst.
       >>> frequency([1, 4, 3, 4, 4], 4)
        3
    """
    return lst.count(search_term)


def flip_case(phrase, to_swap):
    # Flip [to_swap] case each time it appears in phrase.

    lower = "abcdefghijklmnoopqrstuvwxyz"
    caps = lower.upper()
    new_phrase = ""
    for letter in phrase:
        if letter == to_swap:
            if letter in lower:
                new_phrase += letter.upper()
            elif letter in caps:
                new_phrase += letter.lower()
        else:
            new_phrase += letter
    return new_phrase


def multiply_even_numbers(nums):
    # Multiply the even numbers. If there are no even numbers, return 1.

    even_nums = [num*2 for num in nums if num % 2 == 0]
    if even_nums == []:
        return 1
    return even_nums


def capitalize(phrase):
    # Capitalize first letter of first word of phrase.
    return phrase.capitalize()


def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy = lst.copy()
    for item in copy:
        if item != True:
            copy.remove(item)
    return copy


def intersection(l1, l2):
    # Return intersection of two lists as a new list:

    new_l1 = set(l1)
    new_l2 = set(l2)
    l3 = new_l1 & new_l2
    return list(l3)


def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    true_list = []
    false_list = []
    for item in lst:
        if fn(item) == True:
            true_list.append(item)
        else:
            false_list.append(item)
    results = [true_list, false_list]
    return results


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.
    """
    highest_count = 0
    magic_num = 0
    for num in nums:
        count = nums.count(num)
        if count > highest_count:
            highest_count = count
            magic_num = num
    return magic_num


def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """

    if operation == "add":
        total = a+b
        if make_int == True:
            return f'{message} {int(total)}'
        return f'{message} {total}'
    if operation == "subtract":
        total = a-b
        if make_int == True:
            return f'{message} {int(total)}'
        return f'{message} {total}'

    if operation == "multiply":
        total = a*b
        if make_int == True:
            return f'{message} {int(total)}'
        return f'{message} {total}'
    if operation == "divide":
        total = a/b
        if make_int == True:
            return f'{message} {int(total)}'
        return f'{message} {total}'


def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobbies1 = a[2]
    hobbies2 = b[2]
    for hobbies_a in hobbies1:
        for hobbies_b in hobbies2:
            if hobbies_a == hobbies_b:
                return True
    return False


def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter([1, 2, 3, 4])
        [12]

        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter([1, 2])
        []
    """
    filtered = [num*3 for num in nums if num % 4 == 0]
    return filtered
