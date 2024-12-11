# wallet_generator.py
from Blockthon import Wallet, Ethereum, Tron, Dogecoin, Bitcoin, Litecoin, Dash, Digibyte, BitcoinGold, Ravencoin, Qtum, zCash

def generate_wallet_info():
    """
    Gera informações de wallet para várias criptomoedas.
    
    Returns:
        dict: Um dicionário contendo as informações geradas.
    """
    seed = Wallet.getSeed()
    privatekey = Wallet.Bytes_To_PrivateKey(seed)
    mnemonics = Wallet.Bytes_To_Mnemonic(seed, 12)
    wif_compress = Wallet.Bytes_To_Wif(seed, compress=True)
    wif_uncompress = Wallet.Bytes_To_Wif(seed, compress=False)
    dec = Wallet.Bytes_To_Dec(seed)
    xprv = Wallet.Mnemonic_To_RootKey(mnemonics)
    publickey = Wallet.Bytes_To_PublicKey(seed)
    ripemd160 = Wallet.Bytes_To_RIPEMD160(seed)
    compressAddress = Wallet.Bytes_To_Address(seed, compress=True)
    uncompressAddress = Wallet.Bytes_To_Address(seed, compress=False)
    
    # Geração de endereços para Bitcoin
    p2pkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2PKH')
    p2shAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2SH')
    p2wpkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKH')
    p2wshAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSH')
    p2wpkhSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKHinP2SH')
    p2wshSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSHinP2SH')
    
    # Geração de endereços para Litecoin
    p2pkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2PKH')
    p2sh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2SH')
    p2wpkh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WPKH')
    p2wsh_ltc = Litecoin.Address_From_PrivateKey(privatekey, 'P2WSH')
    
    # Geração de endereços para outras criptomoedas
    ethereumAddress = Ethereum.Address_From_PrivateKey(privatekey)
    tronAddress = Tron.Address_From_PrivateKey(privatekey)
    dogeAddress = Dogecoin.Address_From_PrivateKey(privatekey)
    dashAddress = Dash.Address_From_PrivateKey(privatekey)
    digibyteAddress = Digibyte.Address_From_PrivateKey(privatekey)
    RVNAddress = Ravencoin.Address_From_PrivateKey(privatekey)
    QtumAddress = Qtum.Address_From_PrivateKey(privatekey)
    zcashAddress = zCash.Address_From_PrivateKey(privatekey)

    return {
        "Seed": seed,
        "PrivateKey [Hex]": privatekey,
        "Mnemonic": mnemonics,
        "Wif Compressed": wif_compress,
        "Wif UnCompressed": wif_uncompress,
        "Decimal": dec,
        "RIPEMD160": ripemd160,
        "Compressed Address": compressAddress,
        "UnCompressed Address": uncompressAddress,
        "Bitcoin P2PKH": p2pkhAddress,
        "Bitcoin P2SH": p2shAddress,
        "Bitcoin P2WPKH": p2wpkhAddress,
        "Bitcoin P2WSH": p2wshAddress,
        "Bitcoin P2WPKH in Segwit": p2wpkhSegwit,
        "Bitcoin P2WSH in Segwit": p2wshSegwit,
        "Litecoin P2PKH": p2pkh_ltc,
        "Litecoin P2SH": p2sh_ltc,
        "Litecoin P2WSH": p2wsh_ltc,
        "Litecoin P2WPKH": p2wpkh_ltc,
        "Ethereum": ethereumAddress,
        "Tron": tronAddress,
        "Dogecoin": dogeAddress,
        "DASH": dashAddress,
        "DigiByte": digibyteAddress,
        "Ravencoin": RVNAddress,
        "QTUM": QtumAddress,
        "zCASH": zcashAddress,
    }