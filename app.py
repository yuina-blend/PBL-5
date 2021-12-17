import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
os.environ["http_proxy"] = "http://po.cc.ibaraki-ct.ac.jp:3128"
# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# 'hello' を含むメッセージをリッスンします
# 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    print("うんち！")
    say(f"ばなな!")

@app.message("now")
def message_now(message, say):
    print("reqested!")
    say("温度: any, 湿度: any")

# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
