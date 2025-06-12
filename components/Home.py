import streamlit as st
import main

# Check if the user is logged in using session state
if st.session_state.logged_in:
    # Create two tabs: Account Info and Account Settings
    tab1, tab2 = st.tabs(["account info", "account settings"])
    
    # Tab 1: Account Information
    with tab1:
        # Create two columns for layout
        col1, col2 = st.columns(2)
        with col1:
            # Display user's profile image inside a bordered container
            with st.container(border=True):
                st.image(r"images\OIP.jpeg", use_container_width=True)

        with col2:
            # Display user's account information
            st.write("Account Information:")
            st.write(f"Username: {st.session_state.username}")
            st.write(f"Email: {st.session_state.email}")
            st.write(f"Country: {st.session_state.country}")
            st.write(f"Wallet Address: {st.session_state.wallet_id}")
            # Provide a link to the wallet page
            st.page_link(main.wallet_page, label="Click to go to Wallet", icon="💰")
                
    # Tab 2: Account Settings
    with tab2:
        # Create two columns for layout
        col1, col2 = st.columns(2)
        with col1:
            # Display options for logout and wallet activation/deactivation
            st.write("Logout:")
            st.write("Activate/Deactivate Wallet:")
        with col2:
            # Call functions to handle logout and wallet activation/deactivation
            main.logout()
            main.toggle_wallet_activation()
