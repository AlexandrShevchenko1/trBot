from flask import Flask, jsonify
import schedule
import time
import gdown
import aiohttp

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1esYUU3WHPQoWyN4yTT6TBKFec9XllIC7#scrollTo=vU91ottmE1tu', 'colab.ipynb', quiet=False)
    return

# async def request_status():
#     async with aiohttp.ClientSession() as client:
#         async with client.get('https://paper-api.alpaca.markets') as resp:
#             return await resp.json()

def schedule_bot():
    schedule.every(1).minutes.do(run_colab)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
        schedule_bot()