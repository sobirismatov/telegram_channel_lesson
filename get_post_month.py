from read_data import fromJson
data=fromJson("data/result.json")
from datetime import datetime
def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    data=data["messages"]
    a=0
    for i in data:
        if i['type']=='message':
            a+=int(i['date'][5:7]) == month
    return a
print(get_post_month(data,5))
        