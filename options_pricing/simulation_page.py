import streamlit as st
from mc_simulation import Simulation
import matplotlib.pyplot as plt

st.subheader("Monte Carlo Simulation of Individual Stocks")

stocks = ('AAPL', 'NVDA', 'MSFT', 'GOOGL', 'TSLA', 'LCID', 'NFE')
stock_list = st.selectbox("Select Stocks",
                          stocks, )

sim = Simulation(stock_list)
sim = sim.mc_sim_stock_port()
# Plot the results
fig, ax = plt.subplots(figsize=(10, 8))
plt.plot(sim)
ax.set_xlabel("Days")
ax.set_ylabel("Portfolio returns in $")
st.pyplot(fig)
