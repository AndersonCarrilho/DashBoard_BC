import requests
from lxml import html
import time

def getbal(addr0: str) -> str:
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr0
    response_block = requests.get(urlblock)
    byte_string = response_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def balance(addr: str) -> tuple:
    start_time = time.time()  # Inicia o cronômetro
    url_n = f"https://ethbook.guarda.co/api/v2/address/{addr}"
    req = requests.get(url_n)
    response_time = time.time() - start_time  # Calcula o tempo de resposta
    if req.status_code == 200:
        return dict(req.json())["balance"], response_time
    else:
        return "0", response_time

def getBal(addr: str) -> tuple:
    start_time = time.time()  # Inicia o cronômetro
    rl = f"https://btcbook.guarda.co/api/v2/address/{addr}"
    req = requests.get(rl)
    response_time = time.time() - start_time  # Calcula o tempo de resposta
    if req.status_code == 200:
        ret = int(dict(req.json())['balance'])
        return ret / 100000000, response_time  # Converte satoshis para BTC
    else:
        return 0.0, response_time

def GetBalance(address: str) -> tuple:
    start_time = time.time()  # Inicia o cronômetro
    req = requests.get(f"https://btc4.trezor.io/api/v2/address/{address}").json()
    response_time = time.time() - start_time  # Calcula o tempo de resposta
    return dict(req)['balance'], response_time