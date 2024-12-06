import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage User Information", layout="wide")

st.title("🔍 Manage User Information")
st.write("View, update, manage user data, roles, and progression.")

USER_API_URL = "http://api:4000/u"

def fetch_users():
    try:
        response = requests.get(f"{USER_API_URL}/all_users")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user data: {e}")
        return []

# Fetch user data
users = fetch_users()

# Display user data in a table
if users:
    df_users = pd.DataFrame(users)
    st.markdown("### Existing Users")
    st.dataframe(df_users)

    # **Section 1: Update User Progress**
    st.markdown("### Update User Progress")
    user_id = st.selectbox("Select a User to Update:", df_users["user_id"])
    new_progress = st.number_input("Update Progress (0-100):", min_value=0, max_value=100)

    if st.button("Update User Progress"):
        try:
            response = requests.put(f"{USER_API_URL}/{user_id}", json={"progress_percentage": new_progress})
            if response.status_code == 200:
                st.success("User progress updated successfully!")
            else:
                st.error("Failed to update user progress.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error updating user progress: {e}")

    # Add a New User
    st.markdown("### Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    year = st.number_input("Year", min_value=1, max_value=4, step=1)
    plan_id = st.text_input("Plan ID (optional)")

    if st.button("Add User"):
        try:
            response = requests.post(f"{USER_API_URL}/add_user", json={
                "name": name,
                "email": email,
                "year": year,
                "plan_id": plan_id if plan_id.strip() else None
            })
            if response.status_code == 201:
                st.success("User added successfully!")
            else:
                st.error("Failed to add user.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error adding user: {e}")

    # **Section 3: Remove User**
    st.markdown("### Remove a User")
    user_to_remove = st.selectbox("Select a User to Remove:", df_users["user_id"])

    if st.button("Remove User"):
        try:
            response = requests.delete(f"{USER_API_URL}/{user_to_remove}/remove_user")
            if response.status_code == 200:
                st.success("User removed successfully!")
            else:
                st.error("Failed to remove user.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error removing user: {e}")

else:
    st.info("No users found.")
