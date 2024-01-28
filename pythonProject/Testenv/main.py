#install package 
#1. open terminal
#2. type into py -m pip install package_name

# import httpx > lib support web use
# type in terminal to install >> pip install httpx 

import httpx
#from rich import print

# def function to get json n: int return(->) to list of dictionary
def get_cat_ids(n: int)-> list[dict]:
    """Get a list of cat ids from the Cat API"""
    ret = []

    #loop for _ = 0 loop within range(n) from input from get_cat_ids(n)
    for _ in range(n):
        with httpx.Client() as client:
            r = client.get("https://cataas.com/cat?json=true")
            r.raise_for_status()
            # each round will get id and ext value return
            ret.append({
                "id":r.json()["_id"],
                #id represent picture id
                "ext":r.json()["mimetype"].split("/")[-1]
                #ext represent file extension.
                #check pull value from key mimetype': 'image/png', then split by / then get last arg [-1] = png.
            })
    return ret
print(get_cat_ids(3))
"""output > [{'id': 'OaO09ygH0Rjkvxa3', 'ext': 'jpeg'}, 
{'id': 'BzQvoOKv69dw4bor', 'ext': 'jpeg'}, 
{'id': 'mcjTt8SHwJWHFZw6', 'ext': 'jpeg'}]"""



# r =response = get json data  from website
    # r = httpx.get("https://cataas.com/cat?json=true")
    # r.json()
#output r.json()
#{'tags': ['snow', 'fluffy', 'forest cat'], 
# 'createdAt': '2022-05-01T22:09:46.419Z', 
# 'updatedAt': '2022-10-11T07:52:32.699Z', 
# 'mimetype': 'image/png', 'size': 1279080,
# '_id': 'HJ68zaOWi4D0SWoQ'}

# to split file exrension
# s = "image/jpeg"
# s.split("/")[-1]


