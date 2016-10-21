import time
from bs4 import BeautifulSoup
import requests
import os

class main:

    if not os.path.exists('Downloads') : # cria a pastinha downloads se nao existir :D
        os.makedirs('Downloads')
    
    t = 1
    nome_do_arquivo = ' '
    
    
    while True:

        r = requests.get('http://pastebin.com/archive') # Vai na url de arquivos, descobri que apos um tempo pegando
        # o pastebin da ban, mas eu consegui pegar pelo public paste ali do canto :D !

        soup = BeautifulSoup(r.content,'lxml')

        tbl = soup.findAll('a')[10]
        id = tbl.attrs.itervalues().next()
        link = 'http://pastebin.com' + id
    

        split = str(id).split('/')

        if nome_do_arquivo == str(split[1]) :
            time.sleep(3)
            continue

        nome_do_arquivo = str(split[1])

        f = open('Downloads/' + str(split[1]) + '.txt', 'w')

        r = requests.get(link)  # faz um novo get no link recebido

        soup = BeautifulSoup(r.content, 'lxml')

        tbl = soup.findAll('li')

        list_len = len(tbl)

        for i in range(18,list_len) :
         if(len(tbl[i].contents[0]) > 0) :
            f.write(''.join((tbl[i].contents[0].contents[0]).encode('utf-8').strip()))
            f.write('\n')
            
        f.close()
        
        print ("\n" * 100)
        print('===========================================================')
        print('dh.18@msn.com or tone@elitedev.com.br')
        print('===========================================================')
        print('Pastebin public pastes grabber - by Tone - Elite Dev 2016')
        print('===========================================================')
        print('Arquivos baixados: ' + str(t))
        print('===========================================================')
                    
        t = t+1
        time.sleep(3)




