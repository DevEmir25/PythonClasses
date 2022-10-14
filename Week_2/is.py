a = 5
if a is 4:
    print("a equal 4")

if a is not 4:
    print("a is not equal 4")

    """
    Difference between is and equality;

    They are fundamentally different.

    == compares by calling the __eq__ method
    is returns true if and only if the two references are to the same object
    So in comparision with say Java:

    is is the same as == for objects
    == is the same as equals for objects

    """
