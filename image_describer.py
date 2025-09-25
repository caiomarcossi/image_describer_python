import requests
from time import sleep

class ImageDescriber:
	def __init__(self):
		self.analyze_url="https://visionbot.ru/apiv2/res.php"
		self.upload_url="https://visionbot.ru/apiv2/in.php"

	def analyze(self, image_id):
		while True:
			data=requests.get(self.analyze_url, params={"id": image_id})
			if data.status_code == 200:
				result=data.json()
				if result.get("status") == "ok":
					return result.get("text", "Description not found.")
				elif result.get("status") == "fail":
					return "Analysis failed."
			else:
				return f"Error when check the status: {data.status_code}"
			sleep(5)

	def describe(self, image_path):
		try:
			with open(image_path, "rb") as image:
				file_data={"file": ("image.jpg", image, "image/jpeg")}
				params_data={"lang": "en", "target": "image"}
				result=requests.post(self.upload_url, files=file_data, data=params_data)
				if result.status_code == 200:
					result=result.json()
					if result.get("status") == "ok":
						image_id=result.get("id")
						return self.analyze(image_id)
					else:
						return "Error when sending the image for analysis."
				else:
					return f"Error when sending the image: {result.status_code}"
		except FileNotFoundError:
			return "File not found. Please verify the path of the image."
		except requests.exceptions.RequestException as e:
			return f"An error was occurred when sending the request: {e}"
