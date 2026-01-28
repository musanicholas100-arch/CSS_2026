import streamlit as st
import pandas as pd


# Title of the app

st.title(
    "A Study of Programming Language Adoption and Expertise "
    "Across Selected Regions in South Africa"
)


# Researcher information

name = "Mr. Musa Nicholas"
field = "Computer Science"
institution = "North West University"

st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://i.im.ge/2026/01/28/GesTsW.software-developer-6521720-1280.jpeg",
    caption="Computer Science Research"
)

st.divider()


# Publications Section

st.header("Publications")

uploaded_file = st.file_uploader(
    "Upload a CSV of Publications (Title, Authors, Year, Keywords)",
    type="csv"
)

if uploaded_file:
    publications = pd.read_csv(uploaded_file)

    st.subheader("All Publications")
    st.dataframe(publications)

    keyword = st.text_input("Filter publications by keyword")

    if keyword:
        filtered = publications[
            publications.astype(str)
            .apply(lambda col: col.str.contains(keyword, case=False))
            .any(axis=1)
        ]

        st.subheader(f"Filtered Results for '{keyword}'")
        st.dataframe(filtered)

    st.subheader("Publication Trends")

    if "Year" in publications.columns:
        publications["Year"] = pd.to_numeric(
            publications["Year"], errors="coerce"
        )

        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.warning("The CSV must contain a 'Year' column to show trends.")

st.divider()


# Programming Language Research Data

st.header("Programming Language Research Data (South Africa)")

programming_language_data = pd.DataFrame({
    "Programming Language": ["Python", "Java", "C++", "JavaScript", "C#"],
    "Total Users": [1800, 1200, 600, 1500, 900],
    "Total Experts": [520, 430, 210, 380, 300],
    "Gauteng": [700, 480, 260, 520, 350],
    "Western Cape": [450, 300, 140, 420, 230],
    "KwaZulu-Natal": [380, 260, 120, 350, 190],
    "Eastern Cape": [270, 160, 80, 210, 130],
})

st.subheader("Data Viewer")

data_option = st.selectbox(
    "Choose a view",
    [
        "Overview of Programming Languages",
        "Users vs Experts Analysis",
        "Regional Distribution (South Africa)"
    ]
)


# View 1: Overview

if data_option == "Overview of Programming Languages":
    st.subheader("Programming Languages Overview")
    st.dataframe(programming_language_data)


# View 2: Users vs Experts

elif data_option == "Users vs Experts Analysis":
    st.subheader("Users vs Experts per Programming Language")

    st.bar_chart(
        programming_language_data.set_index("Programming Language")[
            ["Total Users", "Total Experts"]
        ]
    )


# View 3: Regional Distribution

elif data_option == "Regional Distribution (South Africa)":
    st.subheader("Regional Contribution by Programming Language")

    region = st.selectbox(
        "Select a Region",
        ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape"]
    )

    regional_data = programming_language_data[
        ["Programming Language", region]
    ].set_index("Programming Language")

    regional_data[region] = pd.to_numeric(
        regional_data[region], errors="coerce"
    )

    st.bar_chart(regional_data)

st.divider()


# Contact Information

st.header("Contact Information")
email = "musanicholas100@gmail.com"
st.write(f"You can reach {name} at {email}.")
