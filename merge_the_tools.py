def merge_the_tools(string, k):
    """
    For a input like AABCAAADA and seperator being an integer like 3
    output should be like
    AB
    CA
    AD
    Need to remove any subsequent occurrences non-distinct characters
    AAB -----> AB
    CAA -----> CA
    ADA -----> AD
    """
    split_string = []
    while string != "":
        split_string.append(string[:k])
        string = string[k:]
    
    for a in split_string:
        output = ""
        for char in a:
            if char not in output:
                output += char
        print(output)

merge_the_tools("AABCAAADA", 3)