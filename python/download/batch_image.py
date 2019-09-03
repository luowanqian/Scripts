import os
import requests
from retrying import retry
from io import BytesIO
from PIL import Image
import progressbar
import concurrent.futures as concurrent


@retry(stop_max_attempt_number=10)
def download(image_url, image_path):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save(image_path)


if __name__ == '__main__':
    base_url = 'http://www.baidu.com'
    num_images = 3
    suffix = '.jpg'
    image_dir = 'images'

    num_workers = 4

    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    with concurrent.ThreadPoolExecutor(max_workers=num_workers) as executor:
        image_urls = []
        image_paths = []
        for image_id in range(num_images):
            url = base_url + '/' + str(image_id + 1) + suffix
            file_path = os.path.join(image_dir, str(image_id + 1) + suffix)
            image_urls.append(url)
            image_paths.append(file_path)

        tasks = {
            executor.submit(download, url, file_path): (url, file_path)
            for url, file_path in zip(image_urls, image_paths)
        }

        i = 0
        total = len(image_urls)
        pbar = progressbar.ProgressBar(max_value=total).start()
        for task in concurrent.as_completed(tasks):
            url, file_path = tasks[task]
            try:
                task.result()
                i = i + 1
                pbar.update(i)
            except Exception as exc:
                print('{} generated an exception: {}'.format(url, exc))
        pbar.finish()
