import streamlit as st
from wallet_generator import generate_wallet_info
from balance_checker import balance, getBal, GetBalance
from alchemy_balance_checker import get_balances

# Adiciona a imagem como banner
st.image("btc_neural/images/fiat-cripto.jpg", use_container_width=True, caption="A Revolução das API's")

# Título do aplicativo
st.title("Sistema Financeiro Cripto-Fiat")
st.write("Selecione uma opção para gerar informações de wallet:")

# Opção de seleção para BTC ou ETH
coin_choice = st.selectbox("Escolha a criptomoeda:", ["BTC", "ETH"])

if coin_choice == "BTC":
    st.write("### Opções para Bitcoin (BTC)")
    action_choice = st.selectbox("Escolha uma ação:", ["Gerar nova wallet", "Consultar wallet existente", "Gerar múltiplas wallets"])

    if action_choice == "Gerar nova wallet":
        if st.button("Gerar Informações da Wallet"):
            wallet_info = generate_wallet_info()
            st.write("### Informações da Wallet")
            st.write(f"**Chave WIF:** {wallet_info['Wif Compressed']}")
            st.write(f"**Endereço BTC:** {wallet_info['Compressed Address']}")
            
            # Consulta o saldo da carteira Bitcoin
            btc_address = wallet_info['Compressed Address']
            btc_balance, btc_response_time = getBal(btc_address)
            st.write(f"**Saldo da carteira BTC:** {btc_balance} BTC")
            st.write(f"**Tempo de resposta:** {btc_response_time:.2f} segundos")

    elif action_choice == "Consultar wallet existente":
        btc_address = st.text_input("Digite o endereço BTC:")
        if st.button("Consultar Saldo"):
            if btc_address:
                btc_balance, btc_response_time = getBal(btc_address)
                st.write(f"**Saldo da carteira BTC:** {btc_balance} BTC")
                st.write(f"**Tempo de resposta:** {btc_response_time:.2f} segundos")
            else:
                st.warning("Por favor, insira um endereço BTC válido.")

    elif action_choice == "Gerar múltiplas wallets":
        num_wallets = st.number_input("Quantas wallets deseja gerar?", min_value=1, max_value=100, value=1)
        if st.button("Gerar Múltiplas Wallets"):
            for _ in range(num_wallets):
                wallet_info = generate_wallet_info()
                st.write("### Informações da Wallet")
                st.write(f"**Chave WIF:** {wallet_info['Wif Compressed']}")
                st.write(f"**Endereço BTC:** {wallet_info['Compressed Address']}")
                
                # Consulta o saldo da carteira Bitcoin
                btc_address = wallet_info['Compressed Address']
                btc_balance, btc_response_time = getBal(btc_address)
                st.write(f"**Saldo da carteira BTC:** {btc_balance} BTC")
                st.write(f"**Tempo de resposta:** {btc_response_time:.2f} segundos")
                st.write("---")  # Separador entre wallets

elif coin_choice == "ETH":

    st.write("### Opções para Ethereum (ETH)")

    action_choice = st.selectbox("Escolha uma ação:", ["Gerar nova wallet", "Consultar wallet existente", "Gerar múltiplas wallets"])


    if action_choice == "Gerar nova wallet":

        if st.button("Gerar Informações da Wallet"):

            wallet_info = generate_wallet_info()

            st.write("### Informações da Wallet")

            st.write(f"**Chave WIF:** {wallet_info['Wif Compressed']}")

            st.write(f"**Endereço ETH:** {wallet_info['Ethereum']}")


            # Consulta o saldo da carteira Ethereum usando balance_checker.py

            eth_address = wallet_info['Ethereum']

            eth_balance, eth_response_time = balance(eth_address)

            st.write(f"**Saldo da carteira ETH:** {eth_balance} ETH")

            st.write(f"**Tempo de resposta:** {eth_response_time:.2f} segundos")


            # Consulta os saldos de USDT e USDC usando a API da Alchemy

            alchemy_balances = get_balances(eth_address)

            st.write("### Saldos de Tokens")

            st.write(f"**Saldo USDT:** {alchemy_balances['USDT Balance']} USDT")

            st.write(f"**Saldo USDC:** {alchemy_balances['USDC Balance']} USDC")


    elif action_choice == "Consultar wallet existente":

        eth_address = st.text_input("Digite o endereço ETH:")

        if st.button("Consultar Saldo"):

            if eth_address:

                # Consulta o saldo da carteira Ethereum usando balance_checker.py

                eth_balance, eth_response_time = balance(eth_address)

                st.write(f"**Saldo da carteira ETH:** {eth_balance} ETH")

                st.write(f"**Tempo de resposta:** {eth_response_time:.2f} segundos")


                # Consulta os saldos de USDT e USDC usando a API da Alchemy

                alchemy_balances = get_balances(eth_address)

                st.write("### Saldos de Tokens")

                st.write(f"**Saldo USDT:** {alchemy_balances['USDT Balance']} USDT")

                st.write(f"**Saldo USDC:** {alchemy_balances['USDC Balance']} USDC")

            else:

                st.warning("Por favor, insira um endereço ETH válido.")


    elif action_choice == "Gerar múltiplas wallets":

        num_wallets = st.number_input("Quantas wallets deseja gerar?", min_value=1, max_value=100, value=1)

        if st.button("Gerar Múltiplas Wallets"):

            for _ in range(num_wallets):

                wallet_info = generate_wallet_info()

                st.write("### Informações da Wallet")

                st.write(f"**Chave WIF:** {wallet_info['Wif Compressed']}")

                st.write(f"**Endereço ETH:** {wallet_info['Ethereum']}")


                # Consulta o saldo da carteira Ethereum usando balance_checker.py

                eth_address = wallet_info['Ethereum']

                eth_balance, eth_response_time = balance(eth_address)

                    

                st.write(f"**Tempo de resposta:** {eth_response_time:.2f} segundos")


                # Consulta os saldos de USDT e USDC usando a API da Alchemy

                alchemy_balances = get_balances(eth_address)

                st.write("### Saldos de Tokens")

                st.write(f"**Saldo USDT:** {alchemy_balances['USDT Balance']} USDT")

                st.write(f"**Saldo USDC:** {alchemy_balances['USDC Balance']} USDC")

                st.write("---")  # Separador entre wallets  

# Adicione mais opções conforme necessário

st.write("### Outras Opções")

if st.button("Serviços de Card e FIAT"):

    st.write("Você selecionou Serviços de Card e FIAT")