import os, time, requests
import scratch_api.scratch_ws_api as scratch3

response = requests.get('https://cs-api.glitch.me/health/')

if response.status_code == 200:
    data = response.json()
    cs_status = data.get("cs_status", "")
    if cs_status == "Not working":
        info = 0
    elif cs_status == "OK":
        info = 1
    else:
        info = None
else:
    print(f"Request failed with status code: {response.status_code}")
    info = None

conn = scratch3.login("Scratch ID", "Scratch PassWord").connect(1107675090, 1, True)

if info is not None:
    conn.send(["1"], [info])
    print(conn.get(["1"]))
else:
    print("No valid info to send.")
