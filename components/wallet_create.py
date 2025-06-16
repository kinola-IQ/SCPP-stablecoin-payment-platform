import streamlit as st
import main
from sqlalchemy import text
import time

if "wallet_balance" not in st.session_state:
    st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
if "recipient" not in st.session_state:
    st.session_state.recipient = ""  # Placeholder for recipient ID

# Function to update the currency balance in the database
def update_currency(currency,amount):
    engine = main.get_database_connection()
    with engine.begin() as conn:
        # Update the currency balance in the database
        conn.execute(
            text(f'update wallets set {currency} = {currency} + :amount where user_id = :user_id'),
            {"amount": amount, "user_id": st.session_state.user_id}
        )

# Function to swap currencies   
def swap_currency(from_currency, to_currency, amount):
    # Placeholder function for currency swap logic
    # This function should implement the actual swap logic
    if from_currency == "NGN" and to_currency == "USD":
        # logic for swapping NGN to USD
        exchange_rate = 0.0025
        converted_amount = amount * exchange_rate
        st.session_state.NGN -= amount
        update_currency("cNGN",-amount)
        st.session_state.USD += converted_amount
        update_currency("USDx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "USD" and to_currency == "NGN":
        # logic for swapping USD to NGN
        exchange_rate = 400
        converted_amount = amount / exchange_rate
        st.session_state.USD -= amount
        st.session_state.NGN += converted_amount
        update_currency("USDx",-amount)
        update_currency("cNGN",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "EUR" and to_currency == "GBP":
        # logic for swapping EUR to GBP
        exchange_rate = 0.85
        converted_amount = amount * exchange_rate
        st.session_state.EUR -= amount
        st.session_state.GBP += converted_amount
        # update the database
        update_currency("EURx",-amount)
        update_currency("GBP",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "GBP" and to_currency == "EUR":
        # logic for swapping GBP to EUR
        exchange_rate = 1.18
        converted_amount = amount / exchange_rate
        st.session_state.GBP -= amount
        st.session_state.EUR += converted_amount
        # Update the wallet balance
        update_currency("GBP",-amount)
        update_currency("EURx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "USD" and to_currency == "EUR":
        # logic for swapping USD to EUR
        exchange_rate = 0.85
        converted_amount = amount * exchange_rate
        st.session_state.USD -= amount
        st.session_state.EUR += converted_amount
        # Update the database
        update_currency("USDx",-amount)
        update_currency("EURx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "EUR" and to_currency == "USD":
        # logic for swapping EUR to USD
        exchange_rate = 1.18
        converted_amount = amount / exchange_rate
        st.session_state.EUR -= amount
        st.session_state.USD += converted_amount
        # Update the database
        update_currency("EURx",-amount)
        update_currency("USDx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "GBP" and to_currency == "USD":
        # logic for swapping GBP to USD
        exchange_rate = 1.35
        converted_amount = amount * exchange_rate
        st.session_state.GBP -= amount
        st.session_state.USD += converted_amount
        # Update the database
        update_currency("GBP",-amount)
        update_currency("USDx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "USD" and to_currency == "GBP":
        # logic for swapping USD to GBP
        exchange_rate = 0.74
        converted_amount = amount * exchange_rate
        st.session_state.USD -= amount
        st.session_state.GBP += converted_amount
        # Update the database
        update_currency("USDx",-amount)
        update_currency("GBP",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "NGN" and to_currency == "EUR":
        # logic for swapping NGN to EUR
        exchange_rate = 0.0022
        converted_amount = amount * exchange_rate
        st.session_state.NGN -= amount
        st.session_state.EUR += converted_amount
        # Update the database
        update_currency("cNGN",-amount)
        update_currency("EURx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "EUR" and to_currency == "NGN":
        # logic for swapping EUR to NGN
        exchange_rate = 450
        converted_amount = amount / exchange_rate
        st.session_state.EUR -= amount
        st.session_state.NGN += converted_amount
        # Update the database
        update_currency("EURx",-amount)
        update_currency("cNGN",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "GBP" and to_currency == "NGN":
        # logic for swapping GBP to NGN
        exchange_rate = 550
        converted_amount = amount / exchange_rate
        st.session_state.GBP -= amount
        st.session_state.NGN += converted_amount
        # Update the database
        update_currency("GBP",-amount)
        update_currency("cNGN",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "NGN" and to_currency == "GBP":
        # logic for swapping NGN to GBP
        exchange_rate = 0.0018
        converted_amount = amount * exchange_rate
        st.session_state.NGN -= amount
        st.session_state.GBP += converted_amount
        # Update the database
        update_currency("cNGN",-amount)
        update_currency("GBP",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "GBP" and to_currency == "EUR":
        # logic for swapping GBP to EUR
        exchange_rate = 1.18
        converted_amount = amount * exchange_rate
        st.session_state.GBP -= amount
        st.session_state.EUR += converted_amount
        # Update the database
        update_currency("GBP",-amount)
        update_currency("EURx",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == "EUR" and to_currency == "GBP":
        # for swapping EUR to GBP
        exchange_rate = 0.85
        converted_amount = amount / exchange_rate
        st.session_state.EUR -= amount
        st.session_state.GBP += converted_amount
        # Update the database
        update_currency("EURx",-amount)
        update_currency("GBP",converted_amount)
        st.session_state.wallet_balance = st.session_state.NGN + st.session_state.USD + st.session_state.EUR + st.session_state.GBP
    if from_currency == to_currency:
        # If the from and to currencies are the same, do nothing
        pass
def fetch_recipient_name(recipient_id):
    engine = main.get_database_connection()
    with engine.begin() as conn:
        recipient_data = conn.execute(
            text("select user_id from wallets where wallet_id = :recipient_id"),
            {"recipient_id": recipient_id}
        ).fetchone()
        if recipient_data:
            user = conn.execute(
                text("select Full_Name from users_registration where user_id = :user_id"),
                {"user_id": recipient_data.user_id}
            ).fetchone()
        st.session_state.recipient = user.Full_Name
    return st.session_state.recipient

# Function to transfer funds between users
def transfer_funds(recipient, amount,currency,recipient_name):
    engine = main.get_database_connection()
    with engine.begin() as conn:
        #transfer funds from one user to another
        #deduct from curren user's wallet
        conn.execute(
            text(f"update wallets set {currency} = {currency} - :amount where user_id = :user_id"),
            {"amount": amount, "user_id": st.session_state.user_id}
        )
        #add to recipient's wallet
        conn.execute(
            text(f"update wallets set {currency} = {currency} + :amount where wallet_id = :recipient_id"),
            {"amount": amount, "recipient_id": recipient}
        )
        st.success(f"Transferred {amount} {currency} to {recipient_name} successfully!")
        time.sleep(1)
        st.rerun()  # Refresh the page to update the wallet balance
        

# Wallet management
# Check if the user is logged in using session state
if st.session_state.logged_in:
    # Check if the user's wallet is active
    if st.session_state.wallet_status == "active":
        # Display wallet title and basic info
        st.title(st.session_state.username + "'s Wallet")
        st.write("Wallet Status:", st.session_state.wallet_status)
        #st.write("Total Balance:", st.session_state.wallet_balance)
        
        # Create tabs for different wallet actions
        Deposit, Swap, Transfer = st.tabs(["Deposit", "Swap", "Transfer"])

        # Deposit tab content
        with Deposit:
            # Split the deposit tab into two columns
            col1, col2 = st.columns(2)
            
            # Right column: currency selection
            with col2:
                with st.container(border=True):
                    st.write("select currency")
                    # Dropdown to select deposit currency
                    deposit_currency = st.selectbox("Currency", ["NGN", "USD", "EUR", "GBP"])
                    # Store selected currency in session state
                    st.session_state.currency_type = deposit_currency
                    left,right = st.columns(2,gap="small")
                    with right:
                        with st.popover("make deposit"):
                                st.write("deposit form")
                                amount = st.number_input("amount", min_value=0, step=1000)
                                if st.button("Deposit"):
                                    if st.session_state.currency_type == "NGN":
                                        st.session_state.NGN += amount
                                        st.session_state.wallet_balance += st.session_state.NGN
                                        update_currency("cNGN",amount)
                                    elif st.session_state.currency_type == "USD":
                                        st.session_state.USD += amount
                                        st.session_state.wallet_balance += st.session_state.USD
                                        update_currency("USDx",amount)
                                    elif st.session_state.currency_type == "EUR":
                                        st.session_state.EUR += amount
                                        st.session_state.wallet_balance += st.session_state.EUR
                                        update_currency("EURx",amount)
                                    elif st.session_state.currency_type == "GBP":
                                        st.session_state.GBP += amount
                                        st.session_state.wallet_balance += st.session_state.GBP
                                        update_currency("GBP",amount)
                                    # Display success message
                                    st.success(f"Deposited {amount} {deposit_currency} successfully!")

                            
            
            # Left column: display selected currency and wallet balance
            with col1:
                st.write("Selected Currency:", st.session_state.currency_type)
                # Display the selected currency type
                if st.session_state.currency_type == "NGN":
                    st.write("NGN Balance:", st.session_state.NGN)
                elif st.session_state.currency_type == "USD":
                    st.write("USD Balance:", st.session_state.USD)
                elif st.session_state.currency_type == "EUR":
                    st.write("EUR Balance:", st.session_state.EUR)
                elif st.session_state.currency_type == "GBP":
                    st.write("GBP Balance:", st.session_state.GBP)
                st.write("total asset in wallet:", st.session_state.wallet_balance)

        # swap tab content
        with Swap:

            st.write("Select currencies to swap and enter the amount.")
            # Example dropdowns for currency selection
            left,middle,right = st.columns(3, gap="small")
            with left:
                from_currency = st.selectbox("From Currency", ["NGN", "USD", "EUR", "GBP"])
            with right:
                to_currency = st.selectbox("To Currency", ["NGN", "USD", "EUR", "GBP"])
            amount = st.number_input("Amount to Swap", min_value=0, step=1000)
            if st.button("Swap"):
                # Placeholder for swap logic
                swap_currency(from_currency, to_currency, amount)
                st.success(f"Swapped {amount} {from_currency} to {to_currency} successfully!")
        
        # Transfer tab content
        with Transfer:
            # Display transfer instructions and form
            st.write("Transfer funds to another user.")
            col1, col2 = st.columns(2)
            with col1:
                # Display current wallet balance
                st.write("Current Wallet Balance:", st.session_state.wallet_balance)
                st.write("Available Currencies:")
                st.write(f"NGN: {st.session_state.NGN}")
                st.write(f"USD: {st.session_state.USD}")
                st.write(f"EUR: {st.session_state.EUR}")
                st.write(f"GBP: {st.session_state.GBP}")
            with col2:
                column1, column2 = st.columns(2)
                with column1:
                    # Display transfer form
                    st.write("\n\nTransfer Form")
                with column2:
                    currency = st.selectbox("Select Currency", ["NGN", "USD", "EUR", "GBP"])
                st.write("Please enter the recipient's ID and the amount to transfer.")
                # Input for recipient 
                recipient = st.text_input("Recipient id")
                # Display the recipient
                if recipient:
                    # Fetch recipient name from the database
                    recipient_name = fetch_recipient_name(recipient)
                    st.write("Recipient Name:", recipient_name)
                else:
                    pass
                # Input for amount to transfer
                amount = st.number_input("Amount to Transfer", min_value=0, step=1000)
                # Button to initiate transfer
                if st.button("Transfer"):
                    # transfer logic
                    if currency == "NGN":
                        if amount > st.session_state.NGN:
                            st.error("Insufficient NGN balance.")
                        else:
                            st.session_state.NGN -= amount
                            update_currency("cNGN",-amount)
                            st.session_state.wallet_balance -= amount
                            transfer_funds(recipient, amount, "cNGN",recipient_name)
                            # st.success(f"Transferred {amount} NGN to {recipient} successfully!")
                    elif currency == "USD":
                        if amount > st.session_state.USD:
                            st.error("Insufficient USD balance.")
                        else:
                            st.session_state.USD -= amount
                            update_currency("USDx",-amount)
                            st.session_state.wallet_balance -= amount
                            transfer_funds(recipient, amount, "USDx",recipient_name)
                            # st.success(f"Transferred {amount} USD to {recipient} successfully!")
                    elif currency == "EUR":
                        if amount > st.session_state.EUR:
                            st.error("Insufficient EUR balance.")
                        else:
                            st.session_state.EUR -= amount
                            update_currency("EURx",-amount)
                            st.session_state.wallet_balance -= amount
                            transfer_funds(recipient, amount, "EURx",recipient_name)
                            # st.success(f"Transferred {amount} EUR to {recipient} successfully!")
                    elif currency == "GBP":
                        if amount > st.session_state.GBP:
                            st.error("Insufficient GBP balance.")
                        else:
                            st.session_state.GBP -= amount
                            update_currency("GBP",-amount)
                            st.session_state.wallet_balance -= amount
                            transfer_funds(recipient, amount, "GBP",recipient_name)
            
    else:
        # Warn user if wallet is not active
        st.warning("Your wallet is not active. Please activate your wallet to use this feature.")