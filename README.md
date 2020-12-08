<h1>Portfolio Automated Analysis</h1>
<p></p>
<p>This repository is the implementation of <a href="https://www.investopedia.com/terms/m/modernportfoliotheory.asp">Modern Portfolio Theory</a>. </p>
<p></p>
<h2>How to use it</h2>
<p>This script collects new data every weekday based on the chosen assets. Every sunday, a script is ran to calculate the optimal allocation for each asset.</p>
<p>There are 3 different outputs sent by email in a single table:</p>
  <li><b>current_position:</b> defines the current allocation to each asset</li>
  <li><b>max_sharpe_position:</b> gives the optimal allocation obtained by maximizing the Sharpe Ratio (higher risk).</li>
  <li><b>current_position:</b> gives the optimal allocation obtained by minimizing the risk</li>
<p></p>
<p></p>
<p>To update the portfolio, please change the following files:</p>
  <li>In folder history, amend portfolio_analysis.ipynb to collect base historical prices for each asset</li>
  <li>Amend the automated_data.py file to collect all new entries of the assets mentioned in the previous file </li>
  <li>Amend the automated_analysis.py file to reflect the current weights.</li>
