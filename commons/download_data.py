import requests
from .find_vcs_root import find_vcs_root
from pathlib import Path

root_dir = find_vcs_root()
s3_url = "https://traffic-data-bucket.s3.amazonaws.com"

def _download_file(suffix, file_name, force):
    forcing_redownload = force
    if Path.exists(root_dir / suffix / file_name) and not forcing_redownload:
        print("{}{} already exists. Use force=True to force redownload".format(suffix, file_name))
    else:
        new_path = root_dir / suffix
        new_path.mkdir(parents=True, exist_ok=True)
        url = s3_url + suffix + file_name
        r = requests.get(url)
        with open(root_dir / suffix / file_name, 'wb') as f:
            f.write(r.content)

def get_TIMS_raw_crashes(force=False):
    _download_file(    
        suffix = "X.Data/raw_data/TIMS_raw_crashes_downloads",
        file_name = "Crashes_2014.csv",
        force = force
    )