import requests
import uuid
import time
import os
import shutil
from termcolor import colored


###############################################################################################################
#                                               CONSTANTES                                                    #
###############################################################################################################

y_list = ['y','Y','yes','YES','Yes']
n_list = ['n','N','no','non','No','NO']

###############################################################################################################
#                                               FONCTIONS                                                     #
###############################################################################################################

def print_centered(s):
    print('\n'*(int(shutil.get_terminal_size().lines/2)))
    print(s.center(shutil.get_terminal_size().columns))


def print_centered_nh(s):
    print(s.center(shutil.get_terminal_size().columns))


def input_centered(s):
    value = input(s.rjust((int(shutil.get_terminal_size().columns))//2))
    return value

def write_file(list_links):
    file = open('codes.txt', 'w')
    for items in list_links:
        file.write(items + "\n")


def gen_tokens(amount,headers,json): # print --> est ce que on affiche les codes /// file --> est ce que on save dans un file?
    list_links = []
    disc_rl = "https://discord.com/billing/partner-promotions/1180231712274387115/"
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    for i in range (int(amount)):
        id = {'partnerUserId': str(uuid.uuid4().hex+uuid.uuid4().hex)}
        x = requests.post(url, headers = headerz, json=id)
        token = x.text[10:]
        token = token[:-2]
        os.system('cls')
        print('Please wait for your tokens to be generated...\nDone : ', i+1)
        
        #print(disc_rl + token)
        list_links.append(disc_rl + token)
        time.sleep(0.1)
    file = open('codes.txt', 'w')
    for items in list_links:
        file.write(items + "\n")
    return list_links


###############################################################################################################
#                                                 MAIN                                                        #
###############################################################################################################


headerz = {
    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105","Chromium";v="119","Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
}

id_or = {'partnerUserId': 'd105bab7abd2c5794e0cedd7a2cc4f256c1b307ccb771adc3e3951f05d897893'}

while True:
    amount = input_centered('Welcome on Croco\'s Nitro Trial Generator.\nPlease enter the desired amount of links : ')
    print('Links will be stored in the \'codes.txt\' file...')
    input('Press Any Key To Continue...')
    gen_tokens(amount,headerz,id_or)
    input('Program ended. Press any key to continue....')
    break