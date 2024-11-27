import multiprocessing
import requests
import os

def download_file(url, name):
    print(f"Start downloading file {name}")
    response = requests.get(url)
    os.makedirs("files", exist_ok=True)  # Ensure the 'files' directory exists
    file_path = f"files/file{name}.jpg"
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"Finished downloading file {name}")

if __name__ == "__main__":
    # URL for the file to be downloaded
    url = "https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=600"

    # List to store process objects
    pros = []

    for i in range(5):
        # Creating a new process for each file download
        p = multiprocessing.Process(target=download_file, args=(url, i))
        p.start()
        pros.append(p)

    # Wait for all processes to finish
    for p in pros:
        p.join()
