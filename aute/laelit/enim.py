def find_points(string, substring):
    """Finds the number of occurrences of a substring in a string.

    Parameters:
    string (str): The string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of occurrences of the substring in the string.
    """
    # Initialize a variable to store the number of matches
    points = 0
    # Loop over the characters of the string
    for i in range(len(string)):
        # Check if the substring matches the current slice of the string
        if string[i:i + len(substring)] == substring:
            # Increment the number of matches
            points += 1
    # Return the number of matches
    return points
