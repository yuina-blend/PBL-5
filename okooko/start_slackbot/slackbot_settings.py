# ライブラリのインポート
import os

# 環境変数に定義しておく
API_TOKEN = os.environ['BOT_API_TOKEN']

# デフォルトの応答
DEFAULT_REPLY = "ばなな！"

PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]
