from tqdm import *
import requests
url = "https://as2.cdn.asset.aparat.com/aparat-video/520055aa72618571e4ce34b434e328b615570838-144p__58945.mp4"
name = "video"
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(name, 'wb') as f:
        pbar = tqdm(total=int(r.headers['Content-Length']))
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                pbar.update(len(chunk))
