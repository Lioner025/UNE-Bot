from pyobigram.client import ObigramClient

blackouts = []
Main = {'Midgar_Einherjar':'Lioner',
        'Warlak_UCI':'Warlak',
        'zartx_02':'Mehlar',
        'Dexthroller':'Nymphetamine',
        'Darksoldcav':'Darksold',
        'VyazenRogue':'Vyazen',
        'Yisus_owo':'Yisus'

       }

def onmessage(update,bot:ObigramClient):
    try:
        username = str(update.message.sender.username)
        msgText = ''
        reply_msg = '🚧 La UNE ha mordido a los siguientes majases 🚧:\n\n'
        main = check_main(username)
        try: msgText = update.message.text
        except:pass

        if '/off' in msgText:
            blackouts.append(username)
            if username != 'Yisus_owo':
                bot.sendMessage(update.message.chat.id,f'A @{username} ({main}) se le fue la corriente.')
            else:
                bot.sendMessage(update.message.chat.id,f'La UNE le Acaba de meter Bankai al maja de Yisus, se lo tiene merecido x carero.')
        elif '/tutorial' in msgText or '/help' in msgText:
            tuto_msg = 'Un bot creado x @Midgar_Einherjar (Lioner) para llevar un registro de los q no tienen luz.\n\n'
            tuto_msg += '🔹 __Comandos:__\n\n   🔸 /off : Te declara sin corriente.\n   🔸 /on : esta de mas explicarlo 😐.\n   🔸 /main (nombre del main)\n    PD: Se deja un espacio entre el comando y el name.\n    🔸 /list : Ver la lista de majases q no tienen luz para reirse de ellos ... y saber q pronto te le vas a sumar 🤣🤣🤣.'
            bot.sendMessage(update.message.chat.id,tuto_msg)
        elif '/main ' in msgText:
            Main[username] = msgText.split()[1]
            bot.sendMessage(update.message.chat.id,f'Se a asignado a "{Main[username]}" como Main de @{username}.')
        elif '/on' in msgText and username in blackouts:
            blackouts.remove(username)
            bot.sendMessage(update.message.chat.id,f'A @{username} ({main}) ya le llego la corriente.')
        elif '/list' in msgText:
            if len(blackouts) != 0:
                for f in blackouts:                   
                    reply_msg += f'🕯 @{f} ({check_main(f)})\n'
                bot.sendMessage(update.message.chat.id,reply_msg)
            else:
                 bot.sendMessage(update.message.chat.id,'No hay nadie sin corriente ?!, y ese milagro ? 🤔.')           
    except Exception as ex:
           bot.sendMessage(update.message.chat.id,f'❌{str(ex)}❌.')

def check_main (username):
    if Main and username in Main:                  
        main = Main[username]
    else:
        main = 'Main no especificado'
    return main

if __name__ == '__main__':
    bot = ObigramClient('1975100501:AAEcCHHCmdGUGApTt-EqpT9tINm9RdyXxlo')
    bot.onMessage(onmessage)
    bot.run()
