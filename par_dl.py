import requests
import os
from concurrent.futures import ThreadPoolExecutor
import argparse

def download_file(url):
    local_filename = os.path.basename(url)
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {url}")

def main():
    parser = argparse.ArgumentParser(description="Download files in parallel from a list of URLs.")
    parser.add_argument("input_file", help="Path to the input file containing one URL per line.")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads for parallel downloading. Default is 20.")
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        urls = f.readlines()

    urls = [url.strip() for url in urls]

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(download_file, urls)

if __name__ == "__main__":
    main()
