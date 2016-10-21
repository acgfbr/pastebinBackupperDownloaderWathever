import time
from bs4 import BeautifulSoup
import requests
import os

class main:

    if not os.path.exists('Downloads') : # cria a pastinha downloads se nao existir :D
        os.makedirs('Downloads')
    
    t = 0 # contador de downs
    nome_do_arquivo = ' ' # nome do arquivo pra verificar se o get foi duplicado [ como to pegando de 3 em 3 seg pode ser que alguem nao enviou nesse tempo ]
    
    while True:

        r = requests.get('http://pastebin.com/archive') # Vai na url de arquivos, descobri que apos um tempo pegando
        # o pastebin da ban, mas eu consegui pegar pelo public paste ali do canto :D !

        id = BeautifulSoup(r.content,'lxml').findAll('a')[10].attrs.itervalues().next() # cata o nome gerado do site pela tag a
        link = 'http://pastebin.com' + id # link final

        split = str(id).split('/') # tira o / do link ex: /AbCdEfG123

        if nome_do_arquivo == str(split[1]) :
            time.sleep(3)
            continue # ignora tudo abaixo e recomeça o loop

        r = requests.get(link)  # faz um novo get no link recebido

        tbl = BeautifulSoup(r.content, 'lxml').findAll('li') # pega as tags li

        conteudo_arquivo = ''
        
        for i in range(18,len(tbl)) : # loopzera pra pegar todo conteudo do arquivo do site
            if(len(tbl[i].contents) > 0) :
                if(len(tbl[i].contents[0]) > 0) :
                    conteudo_arquivo += ''.join((tbl[i].contents[0].contents[0]).encode('utf-8').strip())
                    conteudo_arquivo +='\n'

        if len(conteudo_arquivo) > 0 : # checa se o arquivo foi valido pra download
            f = open('Downloads/' + str(split[1]) + '.txt', 'w')
            f.write(conteudo_arquivo)
            f.close()
            t = t+1

        #gran fenale
            
        print ("\n" * 100)
        print('===========================================================')
        print('dh.18@msn.com or tone@elitedev.com.br')
        print('===========================================================')
        print('Pastebin public pastes grabber - by Tone - Elite Dev 2016')
        print('===========================================================')
        print('Arquivos baixados: ' + str(t))
        print('===========================================================')
                
        time.sleep(3) # 3 segundex
