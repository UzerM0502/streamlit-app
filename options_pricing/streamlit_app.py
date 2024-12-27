import streamlit as st

black_scholes = st.Page(
    page="bs_page.py",
    title="Black Scholes using Monte carlo method"
)

mc_sim = st.Page(
    page="simulation_page.py",
    title="Monte Carlo simulation of individual stocks"
)

pg = st.navigation([black_scholes,
                    mc_sim])
pg.run()
