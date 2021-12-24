import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
os.environ["http_proxy"] = "http://po.cc.ibaraki-ct.ac.jp:3128"
# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

call_count = 0

# 'hello' を含むメッセージをリッスンします
# 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    global call_count
    call_count += 1
    print("うんち！")
    say("ばなな!" + str(call_count))

from th import pin
p = pin(14)

@app.message("!now")
def message_now(message, say):
    global p
    temphumid = p.pinset()
    print(str(temphumid[0]), str(temphumid[1]))
    notice = "温度: " + str(temphumid[0]) + ", 湿度: " + str(temphumid[1])
    print("reqested!")
    say(notice)

@app.message("!poweroff")
def message_poweroff(message, say):
    from PowerControl import PowerControl
    usb = PowerControl()
    usb.usb_power_off()
    say("電源OFF")
    print("power off!")

@app.message("!poweron")
def message_poweron(message, say):
    from PowerControl import PowerControl
    usb = PowerControl()
    usb.usb_power_on(17)
    say("電源ON")
    print("power on!")

@app.message("!exit")
def message_exit(message, say):
    import sys
    sys.exit()

# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
