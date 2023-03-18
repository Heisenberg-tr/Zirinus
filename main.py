#!/usr/bin/env python3



# Zirinus - main.py - 2023/2/28

version = "1.0"
revision = 9

zirinus = """

▒███████▒  ██▓ ██▀███   ██▓ ███▄    █  █    ██   ██████
▒ ▒ ▒ ▄▀░ ▓██▒▓██ ▒ ██▒▓██▒ ██ ▀█   █  ██  ▓██▒▒██    ▒
░ ▒ ▄▀▒░  ▒██▒▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▓██  ▒██░░ ▓██▄
  ▄▀▒   ░ ░██░▒██▀▀█▄  ░██░▓██▒  ▐▌██▒▓▓█  ░██░  ▒   ██▒
▒███████▒ ░██░░██▓ ▒██▒░██░▒██░   ▓██░▒▒█████▓ ▒██████▒▒
░▒▒ ▓░▒░▒ ▓  ░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
░░▒ ▒ ░ ▒ ▒ ░  ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░
░ ░ ░ ░ ░ ▒ ░  ░░   ░  ▒ ░   ░   ░ ░  ░░░ ░ ░ ░  ░  ░
  ░ ░     ░     ░      ░           ░    ░           ░
░

"""

####

main_event_navigation_text = """
    1|  Start
    2|  Options
    3|  Patch Notes

    4|  Exit
    5|  Restart (ReLoad)
"""

main_menu_navigation_text = """
    0| BACK

    1| Spam
    2| Webhook Spam

    3| Command Triggers

    4| View Message Content
    5| Send Message

    6| Set Default Values
    
    7| Presets
"""

settings_navigation_text = """
    0| BACK

    1| General Managament
    2| Security

    3| User Manual

    4| Update Settings
    
"""





try:
    import os
    import sys
    import time
    import threading
    import json
    from datetime import datetime
    import hashlib
except:
    print("Failed to import built-in modules, maybe your Python version isn't supported. If you think this wrong you can open a issue in https://github.com/Heisenberg-tr/Zirinus .")
    if os.system == "NT":
        time.sleep(100009)
    exit()

if os.name == "nt":
    os.system(f"title Zirinus {version}")
else:
    sys.stdout.write(f"\x1b]2;Zirinus {version}\x07")

zirinus_info = f"""
Project Zirinus

VERSION: {version}
REVISION: {revision}

"""

log_file = open("zirinus-logs.log", "w")
log_file.write("=====LOG BEGIN=====\n")
log_file.write(zirinus_info)
def log(level, mess=None):
    global log_file
    current_time = str(datetime.now())[:-3]
    if level == "init":
        return
    if level == "kill":
        log_file.write("\n\n=======LOG END=======\n")
        log_file.close()
    if level == "debug":
        log_message = f" {current_time}  | DEBUG   | {mess} \n"
        log_file.write(log_message)
    if level == "info":
        log_message = f" {current_time}  | INFO    | {mess} \n"
        log_file.write(log_message)
    if level == "warning":
        log_message = f" {current_time}  | WARNING | {mess} \n"
        log_file.write(log_message)
    if level == "error":
        log_message = f" {current_time}  | ERROR   | {mess} \n"
        log_file.write(log_message)

log("init")

log("debug", "Importing required modules...")
try:
    import requests
    import fade
    import colorama
    from colorama import init, Fore, Style
    import cursor
    import shutil
#    import websocket
#    from Cryptodome.Cipher import AES 
#    from Cryptodome.Random import get_random_bytes
    log("debug", "SUCCESS")
except:
    log("error", "Missing modules")
    print("[ ! ] Missing required modules")
    print("Do you want to install them now? (Y/n)")
    choice = str(input(" $ "))
    if choice != "Y" and choice != "y" and choice != "yes":
        exit()
        log("kill")
    else:
        log("info", "Installing missing modules")
    os.system("python3 -m pip install requests")
    os.system("python3 -m pip install fade")
    os.system("python3 -m pip install shutil")
    os.system("python3 -m pip install colorama")
    os.system("python3 -m pip install cursor")
#    os.system("python3 -m pip install websocket-client")  import for discord gateway but it's not ready
#    os.system("python3 -m pip install pycryptodomex") import for AES encryption hut it's not ready
    log("debug", "Attempting to import required modules")
    import shutil
    import cursor
    import requests
    import fade
    import colorama
    from colorama import init, Fore, Style
#    import websocket
#    from Cryptodome.Cipher import AES                                   
#    from Cryptodome.Random import get_random_bytes
    log("debug", "SUCCESS")

init()

try:
    revision_file = open("revision.txt", "r").read().splitlines()
except Exception as e:
    print(f"Cannot read revision file ({e})")
    if os.system == "nt":
        time.sleep(10000)
    sys.exit()


default_input_text = f"{Fore.RED}{Style.BRIGHT}zirinus{Fore.BLUE}@python{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} {Style.RESET_ALL}$ "

def find_average_value_event(self):
    log("info", "MACHINE LEARNING > Find average value")
    return sum(self) / len(self)


def remove_space_event(self = None):
    if self == None:
        return
    self = list(self)
    for i in self:
        for i in self:
            if i == " ":
                self.remove(i)
            if i == "   ":
                self.remove(i)
    self = "".join(self)
    return self

def remove_legacy_components():
    try:
        shutil.rmtree("webhook config")
    except:
        pass
    try:
        legacy_token_file = open("token.txt", "r").read()
        os.remove("token.txt")
        new_token_file = open("tokens.txt", "w")
        new_token_file.write(legacy_token_file)
        new_token_file.close()
    except:
        pass
    try:
        legacy_channelid_file = open("kanal.txt", "r").read()
        os.remove("kanal.txt")
        new_channelid_file = open("channel_ids.txt", "w")
        new_channelid_file.write(legacy_channelid_file)
        new_channelid_file.close()
    except:
        pass

def update_check_event():
    remove_legacy_components()
    print("Checking for updates.. Please wait")
    url = "https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/revision.txt"
    try:
        get_revision = requests.get(url).text
    except:
        return
    if int(get_revision[:1]) >  int(revision):
        print("Update Avalaible")
        print("Updating...")
        print("Pulling file < main.py > ...", end = "")
        main_file = requests.get("https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/main.py").text
        print(main_file)
        
        print("DONE")
        print("Writing to file...", end="")
        with open("main.py", "w") as file:
            file.write(main_file)
        with open("revision.txt", end="") as rev_file:
            rev_file.write(get_revision[:1])

        print("DONE")
        print("Update is finished.")
        exit()
    else:
        print("Already up-to-date")


    



def clear_terminal_event(self = None):
    cursor.hide()
    log("info", "Clearing terminal")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    if self != None:
        print(self)
    cursor.show()

def spam_event(channel_id, auth_token, message, delay):
    if auth_token == "":
        return
    if channel_id == "":
        return
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
            "authorization" : auth_token,
            "user-agent" : "Discord Android",
            "connection" : "keep-alive"
            }
    data = {
            "content" : message
            }
    while True:
        time.sleep(delay)
        message_send_requests = requests.post(url, headers=headers, data=data)
        stat_code = message_send_requests.status_code

        if stat_code == 200:
            log("info", "SPAM > RECEIVED 200 % Do nothing")
            pass
        if stat_code == 401:
            log("info", "SPAM > RECEIVED 401 % Close thread cause: Invalid token")
            print("Invalid token.")
            return
        if stat_code == 403:
            log("info", "SPAM > RECEIVED 403 % Close thread cause: Token have no access to channel")
            print("Access denied")
            return
        if stat_code == 404:
            log("info", "SPAM > RECEIVED 404 % Close thread cause: channel not exist")
            print("Not found")
            return
        if stat_code == 400:
            log("info", "SPAM > RECEIVED 400 % Close thread cause: Client side API rule invalidation")
            print("Server returned forbidden, make sure your message lenght is less than > 2000 <")
            return
        if str(stat_code)[1] == "5":
            log("info", f"SPAM > RECEIVED {stat_code} % Close thread cause: Target server 5xx issue")
            print("Discord side error has been occurred.")
            return
        if stat_code == 429:
            log("info", "SPAM > RECEIVED 429 % Call sleep(1)")
            time.sleep(1)
        if stat_code == 405:
            log("info", "SPAM > RECEIVED 405 % Close thread cause: Client side API method invalidation")
            print("Not allowed.")
            return

def webhook_spam_event(self, arg, url):
    while True:
        time.sleep(arg)
        spam_req = requests.post(url, json=self)
        if spam_req.status_code == 404:
            print("Invalid webhook url")
            log("info", "WHOOK SPAM > RECEIVED 404 % Close thread cause: invalid webhook url")
            return
        if spam_req.status_code == 429:
            log("info", "WHOOK SPAM > RECEIVED 429 % Call sleep(1)")
            time.sleep(1)
        if spam_req.status_code == "400":
            log("info", "WHOOK SPAM > RECEIVED 400 % Close thread cause: Client side API rule invalidation ")
            return

def configure_webhook_event(delay=None, Embed=None, embed_title="<not set>", embed_footer="<not set>", embed_message="<not set>", avatar_url="<not set>", webhook_username="<not set>", plain_message="<not set>"):
    if Embed != None:
        message_type = "embed"
        log("info", "WHOOK CONF > Message type set to embed")
    else:
        message_type = "plain"
        log("info", "WHOOK CONF > Message type set to plain")
    clear_terminal_event()
    print(fade.brazil(zirinus))
    print(f"""                     
Delay : {delay}
Message Type : {message_type}
---
1| Avatar Url : {avatar_url}                           
2| Username : {webhook_username}""")
    if Embed != None:
        print(f"""                        
3| Embed Title : {embed_title}
4| Embed Message : {embed_message}
5| Embed Footer : {embed_footer}                                   

6| Continue""")
    else:
        print(f"""
3| Message : {plain_message}

4| Continue
""")
        
    while True:
        choice = str(input("Enter a number: "))
        choice = remove_space_event(choice)
        if choice == "1":
            avatar_url = str(input("Enter avatar url: "))
            log("info", f"WHOOK CONF > Avatar url has been set to {avatar_url}")
            configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
        if choice == "2":
            webhook_username = str(input("Enter webhook username: "))
            log("info", f"WHOOK CONF > Webhook username has been set to {webhook_username}")
            configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
        if Embed != None:
            if choice == "3":
                embed_title = str(input("Enter embed title: "))
                log("info", f"WHOOK CONF > Embed title has been set to {embed_title}")
                configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
            if choice == "4":
                embed_message = str(input("Enter embed message: "))
                log("info", "WHOOK CONF > Embed message has been set to {embed_message}")
                configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
            if choice == "5":
                embed_footer = str(input("Enter embed footer: "))
                log("info", f"WHOOK CONF > Embed footer has benn set to {embed_footer}")
                configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
            if choice == "6":
                if embed_message == "<not set>":
                    print("embed message field cannot be empty!")
                else:
                    log("info", "WHOOK CONF > Bulding data...")
                    webhook_spam_data_dict = {}
                    webhook_spam_data_dict["embeds"] = [{}]
                    if webhook_username != "<not set>":
                        webhook_spam_data_dict["username"] = webhook_username
                        log("info", "WHOOK CONF > ADD % USERNAME > DATA")
                    if avatar_url != "<not set>":
                        webhook_spam_data_dict["avatar_url"] = avatar_url
                        log("info", "WHOOK CONF > ADD % AVATAR_URL > DATA")
                    if embed_title != "<not set>":
                        webhook_spam_data_dict["embeds"][0]["title"] = embed_title
                        log("info", "WHOOK CONF > ADD % EMBED_TITLE > DATA")
                    webhook_spam_data_dict["embeds"][0]["description"] = embed_message
                    if embed_footer != "<not set>":
                        webhook_spam_data_dict["embeds"][0]["footer"] = {}
                        log("info", "WHOOK CONF > Created empty object for embed_footer")
                        log("info", "WHOOK CONF > ADD % EMBED_FOOTER")
                        webhook_spam_data_dict["embeds"][0]["footer"]["text"] = embed_footer
                    try:
                        log("debug", "WHOOK CONF > Read file - webhook_urls.txt [r]")
                        webhook_url_list = open("webhook_urls.txt", "r").read().splitlines()
                    except Exception as e:
                        log("error", f"WHOOK CONF > Read file action has been terminated due to {e}")
                    for i in webhook_url_list:
                        log("info", "WHOOK CONF > THREAD READY")
                        webhook_spam_thread = threading.Thread(target=webhook_spam_event, args=(webhook_spam_data_dict, delay, i), daemon=True)
                        webhook_spam_thread.start()
                        log("info", "WHOOK CONF > THREAD START ")
                    main_event(mess="[ ! ] Webhook spam started")

        else:
            if choice == "3":
                plain_message = input("Enter message: ")
                log("info", f"WHOOK CONF > ADD % PLAIN_MESSAGE > DATA")
                configure_webhook_event(delay=delay, Embed=Embed, avatar_url=avatar_url, webhook_username=webhook_username, embed_title=embed_title, embed_message=embed_message, embed_footer=embed_footer, plain_message=plain_message)
            if choice == "4":
                if plain_message == "<not set>":
                    print("You need to set a message!")
                else:
                    log("info", "WHOOK CONF > Started to structure data to API acceptable dictionary object...")
                    webhook_spam_data_dict = {}
                    webhook_spam_data_dict["content"] = plain_message
                if webhook_username != "<not set>":
                    webhook_spam_data_dict["username"] = webhook_username
                if avatar_url != "<not set>":
                    webhook_spam_data_dict["avatar_url"] = avatar_url
                webhook_url_list = open("webhook_urls.txt", "r").read().splitlines()
                for i in webhook_url_list:
                    webhook_spam_thread = threading.Thread(target=webhook_spam_event, args=(webhook_spam_data_dict, delay, i), daemon=True)
                    webhook_spam_thread.start()
                    main_event(mess="[ ! ] Webhook spam started!")
                    


        

def webhook_spam_menu_event():
    clear_terminal_event()
    print(fade.brazil(zirinus))
    print("  1|Spam plain message    2|Spam embed message")
    while True:
        message_type = str(input("Message Type (1/2): "))
        message_type = remove_space_event(message_type)
        if message_type == "plain" or message_type == "1":
            embed = None
            break
        if message_type == "embed" or message_type == "2":
            embed = True
            break
        print(" [ ! ] Invalid message type ")
    while True:
        try:
            delay = float(input("Delay: "))
            break
        except:
            print(" [ ! ] Enter a valid number")
    configure_webhook_event(delay=delay, Embed=embed)


def spam_menu_event():
    clear_terminal_event()
    print(fade.brazil(zirinus))
    message = str(input("Message: "))
    while True:
        try:
            delay = float(input("Delay: "))
            break
        except ValueError:
            print("Must be a number!")
    print("Starting...")
    try:
        log("info","SPAM MENU > reading files % tokens.txt^channel_ids.txt")
        with open("tokens.txt", "r") as token_file:
            auth_token = token_file.read().splitlines()
        with open("channel_ids.txt", "r") as channel_id_file:
            channel_id = channel_id_file.read().splitlines()
    except Exception as e:
        print("tokens.txt and channel_ids.txt files not found!")
        print(e)
        log("kill")
        sys.exit()
    for auth in auth_token:
        for cid in channel_id:
            spam_thread = threading.Thread(target=spam_event, args=(cid, auth, message, delay), daemon=True)
            spam_thread.start()
    main_event(mess=" [ ! ] Spam started successfully.")


def message_utils_event(self):
    if self == "send":
        channel_id = str(input("Enter channel ID: "))
        clear_terminal_event()
        try:
            token = open("tokens.txt", "r").read().splitlines()[0]
        except Exception as e:
            main_event(mess=f" [ ! ] Error occurred during reading token file: {e}")
        print("Type :BACK to exit.\n")
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        header = { "authorization" : token }
        while True:
            message = str(input("Enter Message: "))
            if message == ":BACK":
                main_menu_event()
            if message == False: # in progress too
                print("""
            :SWITCH - Switch channel ID
                    
        Append --help to each command to see how it works.
                      """)
            elif message == False: # in progress
                channel_url = f"https://discord.com/api/v9/channels/{channel_id}"
                server_id = requests.get(channel_url, headers=header).json()["guild_id"]
                time.sleep(0.3)
                server_url = f"https://discord.com/api/v9/guilds/{server_id}"
                server_object = requests.get(server_url, headers=header).json()
                final_server_object = f"""
    Server Name : {server_object["name"]}
    Server Description : {server_object["description"]}
    Server Region : {server_object["region"]}

    Roles:
                """
                print(final_server_object)
                for i in server_object["roles"]:
                    print(f"""
        {i["name"]}""")
                    server_channels_object = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels/", headers=header).json()
                    index_count = 0
                    for i in server_channels_object:
                        try:
                            if i[index_count]["ratelimit_per_user"]:
                                pass
                            print("""
        {i[index_count]["name"]}""")
                            index_count = index_count + 1
                        except:
                            index_count = index_count + 1
                            pass
                    print(requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels", headers=header).json())
            elif remove_space_event(message) == "":
                print(" [ ! ] Message cannot be empty")
            else:
                data = { "content" : message }
                post_message = requests.post(url, json=data, headers=header)
                if post_message.status_code == 200:
                    print(f"{Fore.GREEN} | SEND {Style.RESET_ALL}", end="")
                print(post_message.status_code)

    if self == "view":
        channel_id = str(input("Enter channel ID: "))
        clear_terminal_event()
        print("Click CTRL + C to exit.")
        try:
            token = open("tokens.txt", "r").read().splitlines()
            token = token[0]
        except Exception as e:
            main_event(mess=f"Cannot read token file {e}")
        header = {
                "authorization" : token,
                "user-agent" : "Discord Android",
                }
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        message_after = ""
        same_message = False
        message_author_after = ""
        cursor.hide()
        while True:
            
            try:
                time.sleep(0.1)
                message_body = requests.get(url, headers=header)
                if message_body.status_code == 401:
                    cursor.show()
                    main_event(mess="[ ! ] Invalid token")
                if message_body.status_code == 403:
                    cursor.show()
                    main_event(mess="[ ! ] Access denied")
                if message_body.status_code == 429:
                    time.sleep(0.5)
                if message_body.status_code == 400:
                    cursor.show()
                    main_event(mess="[ ! ] Forbidden access")
                message_body = message_body.json()[0]

            except KeyboardInterrupt:
                cursor.show()
                main_menu_event()
                log("info", "MESS UTILS > Received kill signal")
            except EOFError:
                cursor.show()
                main_menu_event()
                log("info", "MESS UTILS > Received kill signal")
            message_author_before = message_body["author"]["id"]
            message_before = message_body["id"]

            message_content = message_body["content"]
            message_author_username = message_body["author"]["username"]
            message_author_tag = message_body["author"]["discriminator"]
            if message_author_after != message_author_before:
                print("—"*25)
            if message_after != message_before:
                print(f"{Fore.RED}{message_author_username}{Fore.BLUE}#{message_author_tag}{Style.RESET_ALL} : {message_content}")
            message_after = message_body["id"]
            message_author_after = message_body["author"]["id"]

def main_menu_event():
    clear_terminal_event()
    cursor.hide()
    print(fade.water(zirinus))
    print(main_menu_navigation_text)
    cursor.show()
    while True:
        choice = str(input(default_input_text))
        choice = remove_space_event(choice)
        if choice == "0":
            main_event()
            break
        if choice == "1":
            spam_menu_event()
            break
        if choice == "2":
            webhook_spam_menu_event()
            break
        if choice == "3":
            print("Coming soon.")
        if choice == "4":
            message_utils_event("view")
            break
        if choice == "5":
            message_utils_event("send")
            break
        if choice == "6":
            print("Coming soon.")
        if choice == "7":
            print("Coming soon.")

        


def settings_manager_event():
    return # settings menu are not ready
    clear_terminal_event()
    cursor.hide()
    print(fade.water(zirinus))
    print(settings_navigation_text)
    cursor.show()
    while True:
        choice = str(input(default_input_text))
        choice = remove_space_event(choice)
        if choice == "0":
            main_event()

        



def main_event(self = None, mess = None, notify = None):
    clear_terminal_event()
    if self != None:
        update_check_event()
    cursor.hide()
    print(fade.fire(zirinus))
    if notify != None:
        print(" ╭――――――――――――――――――", end="")
        print("―"*len(notify["main_text"]), end="")
        print("╮", end="")
        print(f"""

    {notify["header"]}

   {notify["main_text"]}
              """)
        print(" ╰――――――――――――――――――", end="")
        print("-"*len(notify["main_text"]), end="")
        print("╯", end="")
        print("\n\n")
    print(main_event_navigation_text)
    cursor.show()
    if mess != None:
        log("info", "Message event triggered")
        print(f"\n{mess}\n")
    while True:
        choice = str(input(default_input_text))
        choice = remove_space_event(choice)
        if choice == "1":
            main_menu_event()
            break
        if choice == "2":
            print("Coming soon.")
        if choice == "3":
            break
        if choice == "4":
            log("kill")
            sys.exit()
            break
        if choice == "5":
            os.system("python3 main.py")
            sys.exit()
            break

if __name__ == "__main__":
    # Uncomment this to prevent Zirinus from checking updates.
    #main_event(self=None)
    main_event(self=True)
else:
    print("Not designed to import as a module")
    exit()


