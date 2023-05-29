import requests

url = "http://localhost:5000/upload_csv"
file_path = (
    "D:\Github\Tutorials\Flask-Tutorials\JSON_Passing_API_Project\sample_data.csv"
)

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

json_data = response.json()
print(json_data)
