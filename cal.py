import pandas as pd
import argparse
import re

def split_pair(pair):
    match = re.match(r'([A-Z]+)(USDT|BUSD|BTC|ETH|BNB)', pair)
    if not match:
        raise ValueError(f"Invalid pair format: {pair}")
    return match.group(1), match.group(2)

def analyze_trades(file, pair):
    base_coin, quote_coin = split_pair(pair)
    df = pd.read_csv(file)
    filtered_df = df[df['Pair'] == pair].copy()

    filtered_df['Executed_clean'] = filtered_df['Executed'].str.replace(base_coin, '', regex=False).astype(float)
    filtered_df['Amount_clean'] = filtered_df['Amount'].str.replace(quote_coin, '', regex=False).astype(float)
    filtered_df['Fee_clean'] = filtered_df['Fee'].str.replace(base_coin, '', regex=False).astype(float)

    total_executed = filtered_df['Executed_clean'].sum()
    total_amount = filtered_df['Amount_clean'].sum()
    total_fee = filtered_df['Fee_clean'].sum()

    ratio = total_executed / total_amount if total_amount != 0 else 0

    print(f"Results for {pair}:")
    print(f"Total Executed ({base_coin}): {total_executed}")
    print(f"Total Amount ({quote_coin}): {total_amount}")
    print(f"Avg Price: {1/ratio}")
    print(f"Total Fee ({base_coin}): {total_fee}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize Executed, Amount, and Fee for a specific pair.")
    parser.add_argument('--file', type=str, required=True, help='Path to the CSV file.')
    parser.add_argument('--pair', type=str, required=True, help='Trading pair to check, like DOGEUSDT or BTCUSDT.')
    args = parser.parse_args()

    analyze_trades(args.file, args.pair)

