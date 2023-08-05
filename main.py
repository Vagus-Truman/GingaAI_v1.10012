from app.discord_bot.discord_api import client, discord_token

if __name__ == "__main__":
    client.run(discord_token)
    
# use this in terminal to get the webspace open
# pip install llama-cpp-python[server]
# $env:MODEL = "[Insert Model Path]"

# $env:MODEL = "C:\Users\Kenne\Desktop\Ginga_AI\.bin files\llama-2-13b-chat.ggmlv3.q4_K_M.bin"
# python -m llama_cpp.server