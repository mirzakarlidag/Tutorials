from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
def csv_to_json():
    df = pd.read_csv("sample_data.csv")  # Read the CSV file into a pandas DataFrame

    # Perform any necessary processing on the DataFrame

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient="records")

    return df


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
