import streamlit as st
import time
import pandas as pd
from sqlalchemy import create_engine, text
import urllib

# Cached database connection for efficiency
@st.cache_resource
def get_database_connection():
    # ODBC connection string for SQL Server
    odbc_str = (
    "mssql+pyodbc://@DESKTOP-H2S6EIU/stablecoin"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
    )
    engine = create_engine(odbc_str)

    # # URL encode the connection string
    # connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(odbc_str)}"
    # engine = create_engine(
    #     connection_url,
    #     pool_pre_ping=True,
    #     pool_size=5,
    #     max_overflow=10,
    #     connect_args={"timeout": 30}
    # )
    return engine

# Initialize session state for login status if not already set
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Initialize session state for user data if not already set
if "user_id" not in st.session_state:
    st.session_state.user_id = 0
if "username" not in st.session_state:
    st.session_state.username = "Guest"
if "password" not in st.session_state:
    st.session_state.password = "********"
if "country" not in st.session_state:
    st.session_state.country = "none"
if "email" not in st.session_state:
    st.session_state.email = "@example.com"
if "wallet_status" not in st.session_state:
    st.session_state.wallet_status = "None"
if "currency_type" not in st.session_state:
    st.session_state.currency_type = "None"
if "NGN" and "GBP" and "USD" and "EUR" not in st.session_state:
    st.session_state.NGN = 0.0
    st.session_state.GBP = 0.0
    st.session_state.USD = 0.0
    st.session_state.EUR = 0.0


# Login function
def login():
    if st.button("Login"):
        st.session_state.logged_in = True
        progress_text = " Logging you in. Please wait."
        engine = get_database_connection()
        with engine.connect() as con:
            # Check if user exists with provided email and password
            existing_user = pd.read_sql(
                "SELECT * FROM users_registration WHERE email = ? AND Password = ?",
                con=con,
                params=(st.session_state.email, st.session_state.password)
            )
            if not existing_user.empty:
                # Show spinner while logging in
                with st.spinner(text=progress_text, show_time=True):
                    time.sleep(1.5)
                st.success("You are now logged in!")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("Invalid email or password.")
                st.session_state.logged_in = False

# Logout function
def logout():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("You are now logged out!")
        st.rerun()

# Deactivate wallet function
def toggle_wallet_activation():
    if st.button("Toggle Wallet Activation"):
        engine = get_database_connection()
        with engine.connect() as con:
            con.execute(
                text("UPDATE wallets SET wallet_status = CASE WHEN wallet_status = 'active' THEN 'suspended' ELSE 'active' END WHERE user_id = :user_id"),
                {"user_id": st.session_state.user_id}
            )
            wallet_status = con.execute(
                text("SELECT wallet_status FROM wallets WHERE user_id = :user_id"),
                {"user_id": st.session_state.user_id}
            ).fetchone()
            st.session_state.wallet_status = wallet_status.wallet_status
        if st.session_state.wallet_status == "active":
            st.success("Your wallet has been activated.")
        else:
            st.success("Your wallet has been suspended.")


# Define pages using Streamlit's Page API
home_page = st.Page(lambda: None, title="Login")  # placeholder, home handled in main below

profile_page = st.Page(
    page=r"components/Home.py",
    title="Profile",
    icon="👤"
)

wallet_page = st.Page(
    page=r"components/wallet_create.py",
    title="Wallet",
    icon="💰"
)

dashboard_page = st.Page(
    page=r"components/Dashboard.py",
    title="Dashboard",
    icon="📊"
)


history_page = st.Page(
    page=r"components/Transaction_History.py",
    title="History",
    icon="📜"
)

# Navigation logic based on login status
if st.session_state.logged_in:
    # Show navigation menu if logged in
    page = st.navigation(
        {
            "Profile": [profile_page],
            "Account": [wallet_page],
            "Report": [dashboard_page, history_page],
        }
    )

    page.run()
    
else:
    # Show login/register UI if not logged in
    st.title("Welcome to Interstellar Crypto Payment Platform")
    st.write("Please log in to access the platform features.")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # Login tab
    with tab1:
        st.write("Please enter your login details below.")
        email = st.text_input("Email", placeholder="Enter your email", key="email_login")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="password_login")
        st.session_state.email = email
        st.session_state.password = password
        # Check if user exists in the database
        engine= get_database_connection()
        with engine.connect() as con:
            existing_user = con.execute(
                text("SELECT user_id, Full_Name, country, email FROM users_registration WHERE email = :email"),
                {"email": st.session_state.email}
            )
            user_data = existing_user.fetchone()
            st.session_state.user_id = user_data.user_id if user_data else 0
            wallet_data = con.execute(
                        text("select * from wallets where user_id = :user"),
                        {"user": st.session_state.user_id}
                    )
            wallet_data = wallet_data.fetchone()
            # Check if wallet exists for the user
            if user_data:
                # Update session state with retrieved user data
                st.session_state.logged_in = True
                st.session_state.username = user_data.Full_Name
                st.session_state.country = user_data.country
                st.session_state.email = user_data.email
                st.session_state.wallet_status = wallet_data.wallet_status
                st.session_state.NGN = wallet_data.cNGN
                st.session_state.GBP = wallet_data.GBP
                st.session_state.USD = wallet_data.USDx
                st.session_state.EUR = wallet_data.EURx
                st.session_state.wallet_id = wallet_data.wallet_id
                # Call login logic
                login()

            elif user_data is None:
                st.error("User does not exist. Please register first.")
                st.session_state.logged_in = False
                
    # Registration tab
    with tab2:
        st.write("Please fill in the details below to register.")
        #accept user input for registration

        # Full name
        username = st.text_input("Username", placeholder="Enter your username")
        st.session_state.username = username

        #email
        email = st.text_input("Email", placeholder="Enter your email", key="email_register")
        st.session_state.email = email

        #password
        try:
            password = st.text_input("Password", type="password", placeholder="Enter your password", key="password_register")
            if len(password) == 8:
                st.session_state.password = password

            if len(password) < 8:
                st.warning("Password must be at least 8 characters long.")
                st.session_state.logged_in = False
            elif len(password) > 8:
                st.warning("Password must not exceed 8 characters.")
                st.session_state.logged_in = False
        except ValueError:
            st.error("Invalid password input. Please enter a valid password.")

        #country selection
        country = st.selectbox(
            "Country",
            placeholder="Select your country",
            options=["Nigeria", "USA", "UK", "France"],
            key="country_register",
            )
        st.session_state.country = country

        # Handle sign up button click
        if st.button("Sign up"):
            progress_text = " Signing you in. Please wait."
            engine = get_database_connection()
            with engine.connect() as con:
                # Check if user already exists
                existing_user = pd.read_sql(
                    "SELECT * FROM users_registration WHERE email = ?",
                    con=con,
                    params=(st.session_state.email,)
                )
                if existing_user.empty:
                    # Insert new user into users_registration table
                    with engine.begin() as con:
                        con.execute(
                            text(
                                "INSERT INTO users_registration (Full_name, email, Password,country) "
                                "VALUES (:user, :email, :pwd, :country)"
                            ),
                            {
                                "user": st.session_state.username,
                                "email": st.session_state.email,
                                "pwd": st.session_state.password,
                                "country": st.session_state.country
                            }
                        )
                    # Create a wallet for the new user if not exists
                    with engine.begin() as con:
                        # Check if the wallet already exists
                        existing_wallet = pd.read_sql(
                            "SELECT * FROM wallets WHERE email = ?",
                            con=con,
                            params=(st.session_state.email,)
                        )
                        if existing_wallet.empty:
                            with engine.begin() as con:
                                result = con.execute(
                                    text("SELECT user_id FROM users_registration WHERE email = :email"),
                                    {"email": st.session_state.email}
                                )
                                user = result.fetchone()

                                if user:
                                    if "currency_type" in st.session_state:
                                        if st.session_state.country == "Nigeria":
                                            st.session_state.currency_type = "NGN"
                                        elif st.session_state.country == "USA":
                                            st.session_state.currency_type = "USD"
                                        elif st.session_state.country == "UK":
                                            st.session_state.currency_type = "GBP"
                                        else:
                                            st.session_state.currency_type = "EUR"
                                    # Insert new wallet for the user
                                    con.execute(
                                        text(
                                            "INSERT INTO wallets (user_id, email, wallet_status) "
                                            "VALUES (:user_id, :email, 'active')"
                                        ),
                                        {
                                            "user_id": user.user_id,
                                            "email": st.session_state.email,
                                        }
                                    )
                    # Update wallet session state with new user data
                    with engine.connect() as con:
                        wallet_data = con.execute(
                            text("SELECT * FROM wallets WHERE email = :email"),
                            {"email": st.session_state.email}
                        ).fetchone()
                        #update session state with wallet data
                        st.session_state.wallet_status = wallet_data.wallet_status
                    st.success("User created successfully! You can now log in.")
                    # Show spinner and log in the user
                    with st.spinner(text=progress_text, show_time=True):
                        time.sleep(1.5)
                    st.session_state.logged_in = True
                    st.success("You are now logged in!")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error("User already exists.")
                    st.session_state.logged_in = False
