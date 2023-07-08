import requests

def download_videos():
    for i in range(0, 3000):
        url = f"https://dp-vids.com/contents/videos/0/{i}/{i}.mp4"
        response = requests.get(url)
        if response.status_code == 200:
            filename = f"video_{i}.mp4"
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Video not found for URL: {url}")

if __name__ == "__main__":
    download_videos()
