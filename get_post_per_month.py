from read_data import fromJson
data=fromJson("data/result.json")
import datetime
def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    data=data["messages"]
    a=[]
    for i in data:
        if i["date"].month>=5:
            a.append(i["date"])

    return a
print(get_post_per_month(data))
