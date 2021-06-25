import random ,discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODU2MTI0NzQzOTg3NjI1OTg0.YM8eTA.Zn9fvfGv3LVGZsj3unEXR0MNJTQ'

# 接続に必要なオブジェクトを生成
client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
hina = open("hina.txt", "r").read().splitlines()
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    global hina
    if message.content.startswith("!hina"):
        await message.channel.send(random.choice(hina))
    if message.content.startswith("!upload"):
        hina = open("hina.txt", "r").read().splitlines()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
