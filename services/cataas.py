import httpx


def get_cat_ids(n: int)->list[dict]:
    ret = []
    with httpx.Client() as client:
        for _ in range(n):
                    r = client.get("https://cataas.com/cat?json=true")
                    r.raise_for_status()
                    ret.append({
                        "id": r.json()["_id"],
                        "ext": r.json()["mimetype"].split("/")[-1]
                    })
    return ret


def download_cats(n: int) -> None:
    """
    Download  a list of cats from the cataas API.
    """
    cat_ids = get_cat_ids(n)
    with httpx.Client(timeout=10) as client:
        for cat_id in cat_ids:
            r = client.get(f"http//cataas.com/cat/{cat_id['id']}")
            r.raise_for_status()
            with open(f"out/cats/{cat_id['id']}.{cat_id['ext']}","wb") as f:
                #open blank folder name out and write file content with name cat ID and file extension.
                f.write(r.content)

