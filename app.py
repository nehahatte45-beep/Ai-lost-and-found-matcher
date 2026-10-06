import streamlit as st
from database import create_table, add_item, get_items
from matcher import find_match

# Create database table
create_table()

st.set_page_config(
    page_title="AI Lost & Found Matcher",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Lost & Found Matcher")
st.write("Find lost and found items using AI.")

# Sidebar
menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Home",
        "Report Lost Item",
        "Report Found Item",
        "Find Match"
    ]
)


# Home
if menu == "Home":

    st.header("Welcome!")

    st.write("""
    This application uses AI to match lost and found items.

    Users can:
    - Report lost items
    - Report found items
    - Find possible matches using Gemini AI
    """)


# Report Lost Item
elif menu == "Report Lost Item":

    st.header("📱 Report Lost Item")

    name = st.text_input("Item Name")

    description = st.text_area(
        "Description"
    )

    location = st.text_input(
        "Lost Location"
    )

    date = st.date_input(
        "Lost Date"
    )

    contact = st.text_input(
        "Contact Number"
    )

    if st.button("Submit Lost Item"):

        if name and description and location and contact:

            add_item(
                "Lost",
                name,
                description,
                location,
                str(date),
                contact
            )

            st.success(
                "Lost item reported successfully!"
            )

        else:

            st.warning(
                "Please fill all required fields."
            )


# Report Found Item
elif menu == "Report Found Item":

    st.header("📦 Report Found Item")

    name = st.text_input("Item Name")

    description = st.text_area(
        "Description"
    )

    location = st.text_input(
        "Found Location"
    )

    date = st.date_input(
        "Found Date"
    )

    contact = st.text_input(
        "Contact Number"
    )

    if st.button("Submit Found Item"):

        if name and description and location and contact:

            add_item(
                "Found",
                name,
                description,
                location,
                str(date),
                contact
            )

            st.success(
                "Found item reported successfully!"
            )

        else:

            st.warning(
                "Please fill all required fields."
            )


# Find Match
elif menu == "Find Match":

    st.header("🤖 AI Lost & Found Matcher")

    found_name = st.text_input(
        "Found Item Name"
    )

    found_description = st.text_area(
        "Found Item Description"
    )

    found_location = st.text_input(
        "Found Location"
    )

    found_date = st.date_input(
        "Found Date"
    )

    if st.button("🔍 Find AI Match"):

        if found_name and found_description:

            found_item = f"""
Name: {found_name}
Description: {found_description}
Location: {found_location}
Date: {found_date}
"""

            # Get all lost items
            lost_items = get_items("Lost")

            if lost_items:

                result = find_match(
                    found_item,
                    lost_items
                )

                st.subheader("🎯 AI Matching Result")

                st.write(result)

            else:

                st.warning(
                    "No lost items found in database."
                )

        else:

            st.warning(
                "Please enter the item name and description."
            )