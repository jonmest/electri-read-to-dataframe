# How to use the [Electri API](https://rapidapi.com/jonmester3/api/electri) to read day-ahead electricity prices for the EU into a Pandas DataFrame
This is a short example, in Python 3, on how you can use [Electri API](https://rapidapi.com/jonmester3/api/electri) to read electricity prices and convert the data into a Pandas Dataframe. To get the short story, just check out `main.py`.

## Dependencies
To run the script, you need `pandas` and `requests` installed. To quickly get going, open your terminal and run:
```shell
pip install -r requirements.txt
```

## Running the script
The script depends on you providing an API key for Electri, which you can get for free [here](https://rapidapi.com/jonmester3/api/electri). Then, you need to set it as an environment variable when running the script. For example:
```shell
API_KEY=<your-api-key> python main.py
```

