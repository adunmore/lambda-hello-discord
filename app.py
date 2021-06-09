import os

from flask import Flask, request
from flask_discord_interactions import DiscordInteractions

from apig_wsgi import make_lambda_handler

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]

@discord.command()
def ping(ctx):
    # breakpoint()
    "Respond with a friendly 'pong'!"
    return "Pong!"

discord.set_route("/interactions")

discord.update_slash_commands(guild_id=os.environ["GUILD_ID"])

handler = make_lambda_handler(app)

if __name__ == '__main__':
    app.run()