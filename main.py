import pandas as pd
import argparse
from datetime import timedelta, datetime

def config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./sample_data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./sample_data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./sample_data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):
    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return

def getStartDate(fname):
    consumption = pd.read_csv(fname)
    time = consumption['time'].to_numpy()[-1]
    date = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    
    start = date + timedelta(hours=1)

    return start.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    args = config()

    date = getStartDate(args.consumption)

    data = [[date, "buy", 2.5, 3],
            [date, "sell", 3, 5]]
    output(args.output, data)