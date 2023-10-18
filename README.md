# Parallel File Downloader

A simple python script to download multiple files in parallel from a list of URLs. This tool uses the `requests` library for fetching the content and `ThreadPoolExecutor` for parallel downloading.  

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Usage](#setup-and-usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Command-line interface for flexible usage.
- Downloads files in parallel to speed up the process.
- Supports customization of the number of download threads.
- Downloads large files in chunks, minimizing memory usage.

## Prerequisites

Before running the script, ensure you have:

- Python (version 3.6 or newer)
- `requests` library 

Install the required library using `pip`:

```bash
pip install requests
```

## Setup and Usage

1. Clone this repository:

```bash
git clone https://github.com/mbm6448/parallel_URL_dl.git
cd parallel_URL_dl
```

2. Create a file with your desired name (e.g., `urls.txt`). Populate it with URLs — one URL per line.

3. Run the script with:

```bash
python downloader.py urls.txt
```

For specifying the number of threads:

```bash
python downloader.py urls.txt --threads 10
```

The downloaded files will be saved in the same directory using their original filenames from the URLs.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mbm6448/parallel_dl/issues) or open a new issue for any feedback or suggestions.

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
