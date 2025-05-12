# Binance Accurate Trade Analyzer (BAT Analyzer)

Accurate average price & fee analyzer for Binance trade history — Fix average price blind spots after cold wallet transfers.

---

## Why this tool?

Binance's **app average price becomes misleading when:**
- You move crypto to cold wallets.
- You later buy more crypto.
- Binance shows only the average of current holdings, ignoring past transfers.

Additionally:
- Binance only displays **6 months of trade history** in the UI.
- You can export the full history, but Binance still **doesn't correct the average price**.

---

## This tool solves that.

**Binance Accurate Trade Analyzer (BAT Analyzer)**:
- 🧾 Reads your **exported Binance full trade history CSV**.
- 📊 Calculates **true executed quantity**, **total amount spent**, and **actual fees paid**, **ignoring transfers to cold wallets**.
- 💡 Gives you a **clean, accurate average price**, protecting you from Binance's misleading calculations.


---

## 📈 Example Use Case

You transferred 0.1 BTC to your cold wallet. Later, you bought 0.05 BTC on Binance.
Binance app shows your average based on 0.05 BTC only, ignoring your previous buys.
This tool recalculates based on **all trades**, regardless of transfer, to show your **true cost per BTC**.

---

## 🚀 Quick Start:

### 1. Export your Binance trade history (CSV).

### 2. Run the analyzer:
```bash
python cal.py --file example.csv --pair BTCUSDT
# You can replace the example.csv to your own trade history, and replace BTCUSDT to whether pair included in your trade history.
```
### 3. Get clean, accurate results:
```bash
Results for BTCUSDT:
Total Executed (BTC): 0.00583
Total Amount (USDT): 308.59939999999995
Avg Price: 52933.001715265855
Total Fee (BTC): 5.83e-06
```

---

## Install Requirements
```bash
pip install -r requirements.txt
```


