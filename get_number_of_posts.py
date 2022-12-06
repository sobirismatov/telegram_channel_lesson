from read_data import fromJson
data=fromJson("data/result.json")
def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    data=data["messages"]
    return len(data)
print(get_number_of_posts(data))