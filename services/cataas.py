import httpx


def get_cat_ids(n: int)->list[dict]:
    ret = []
    for _ in range(n):
        with httpx.Client() as client:
            r = client.get("https://cataas.com/cat?json=true")
            r.raise_for_status()
            ret.append({
                "id": r.json()["_id"],
                "ext": r.json()["mimetype"].split("/")[-1]
        })
    return ret
