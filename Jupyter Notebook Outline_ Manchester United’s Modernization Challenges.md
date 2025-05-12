# Jupyter Notebook Outline: Manchester United’s Modernization Challenges

**(Focus: Recruitment Strategy & On-Pitch Performance)**

## 1. Introduction

*   **Objective**: Clearly state the goal: To analyze Manchester United’s recruitment strategy and on-pitch performance, proposing data-driven strategies for improvement. Emphasize that this case study is designed to showcase analytical skills to potential employers.
*   **Context**: Briefly provide background on Manchester United's recent challenges and the competitive landscape of modern football.
*   **The Role of Data Analytics**: Highlight the increasing importance of data analytics in gaining a competitive edge in football operations, from recruitment to tactical decisions.

## 2. Deep Dive: Recruitment & Squad Analysis

*   **2.1. Data-Driven vs. Legacy Signings: A Comparative Analysis**
    *   **Methodology**: Explain how signings will be categorized and evaluated (e.g., using pre-defined performance metrics, cost-benefit analysis).
    *   **Successful Data-Backed Signings**: 
        *   In-depth analysis of players like Lisandro Martínez and André Onana. Include specific metrics (e.g., Martínez: tackles/90, interception rate, pass completion % under pressure; Onana: long pass accuracy, saves from xG conceded, sweeping actions).
        *   Discuss how their profiles matched team needs identified through data.
    *   **Inefficient Legacy/Reputation-Based Signings**:
        *   Detailed examination of players like Jadon Sancho and Antony. Include metrics (e.g., Sancho: G/A per 90, key passes/90, successful dribbles/90 vs. cost; Antony: shot conversion rate, xG per shot, possession loss rate).
        *   Analyze the financial implications (wages, amortization) versus on-pitch returns.
    *   **Mock Visualization 1**: Scatter Plot - "Transfer Fee vs. On-Pitch Value (Composite Metric)".
        *   *Description*: X-axis: Transfer Fee. Y-axis: A composite performance score (e.g., weighted average of G/A, xG contribution, defensive actions relevant to position). Highlight successful (high value, lower/justified cost) and unsuccessful (low value, high cost) signings. Different colors/shapes for data-driven vs. legacy signings.
    *   **Python Code Snippet 1**: Data Processing for Player Evaluation.
        *   *Description*: Provide a Pandas snippet demonstrating how to load player data (from a hypothetical CSV), calculate a simple composite performance score, or filter players based on certain criteria relevant to recruitment.
        ```python
        # Example: Calculate Cost per Goal Contribution
        # import pandas as pd
        # df['cost_per_G_A'] = df['transfer_fee_millions'] / (df['goals'] + df['assists'])
        # print(df[['player_name', 'cost_per_G_A']].sort_values(by='cost_per_G_A'))
        ```
*   **2.2. Youth Academy Impact: A Missed Opportunity?**
    *   **Quantitative Analysis**: Compare the number of academy graduates in the first team, minutes played, and contributions (G/A, key roles) against top competitors (e.g., Man City, Chelsea, Barcelona) and United's own successful eras.
    *   **Financial & Sporting Benefits**: Discuss the cost savings from promoting youth and the cultural impact on the club.
    *   **Link to Recruitment**: Analyze how a less productive academy might increase pressure on external recruitment and inflate transfer spending.
*   **2.3. The Recruitment Process: Identifying Bottlenecks**
    *   **Current Structure (Hypothesized)**: Briefly discuss the typical structure of a football club's recruitment department and where Man Utd might align or differ.
    *   **Areas for Data Integration**: Identify specific stages in the recruitment pipeline (talent identification, scouting, shortlisting, final decision) where data analytics can be more deeply embedded.
    *   **Benchmarking**: Compare with clubs known for strong data-led recruitment (e.g., Brighton, Brentford, Liverpool), highlighting their processes or tools (if publicly known).

## 3. Deep Dive: On-Pitch Performance Metrics

*   **3.1. Defensive Vulnerabilities: A Statistical Breakdown**
    *   **Key Metrics**: Analyze Goals Conceded, Expected Goals Against (xGA), shots conceded (volume and quality), defensive actions (tackles, interceptions, clearances per 90), and pressing efficiency (PPDA – Passes Per Defensive Action).
    *   **Trend Analysis**: Show trends over recent seasons or compare against league averages/top performers.
    *   **Link to Recruitment/Squad Composition**: Discuss if defensive weaknesses correlate with specific player profiles lacking or underperforming in the squad (e.g., lack of a dominant defensive midfielder, specific fullback attributes).
    *   **Mock Visualization 2**: Defensive Performance Dashboard Snippet.
        *   *Description*: A small multi-panel visual showing: (a) Trend line of xGA vs. Actual Goals Conceded per match. (b) Bar chart comparing Man Utd's PPDA with top 4 PL teams. (c) A zone map of the pitch showing where most shots are conceded from.
*   **3.2. Attacking Dynamics: Unpacking the Numbers**
    *   **Core Metrics**: Analyze Expected Goals (xG), actual goals scored, shot volume and quality (xG per shot), conversion rates, key passes, progressive passes, and xG Buildup/xG Chain involvement.
    *   **Player Contributions**: Break down attacking contributions by key players (e.g., Fernandes, Højlund, Rashford) and assess if recruitment has supplied the necessary creative and finishing talent.
    *   **Tactical Implications**: Discuss how these metrics reflect the team's attacking style and effectiveness.
    *   **Python Code Snippet 2**: Generating a Basic Shot Map.
        *   *Description*: Provide a Matplotlib/Seaborn snippet to plot shot locations on a pitch outline from x,y coordinates, color-coding by outcome (goal, save, miss) or xG value.
        ```python
        # Example: Basic Shot Map (requires pitch outline function and shot data)
        # import matplotlib.pyplot as plt
        # import seaborn as sns
        # # Assuming 'shots_df' has 'x', 'y', 'is_goal' columns
        # fig, ax = plt.subplots()
        # # draw_pitch(ax) # User-defined function to draw a football pitch
        # sns.scatterplot(data=shots_df, x='x', y='y', hue='is_goal', ax=ax)
        # plt.title('Shot Map')
        # plt.show()
        ```
*   **3.3. Player Fitness and Availability: The Hidden Cost**
    *   **Data Points**: Analyze total injuries, days lost to injury, types of injuries (muscle, impact), and recurrence rates. Compare with league averages or competitors.
    *   **Impact Analysis**: Quantify the impact of injuries on team selection consistency, performance, and financial cost (lost wages for unavailable players).
    *   **Link to Recruitment & Training**: Discuss if recruitment strategies consider player injury history sufficiently, or if training loads/methodologies might be contributing factors.
    *   **Mock Visualization 3**: Injury Impact Chart.
        *   *Description*: A stacked bar chart showing minutes lost per month due to injury, broken down by player position or injury type. Alternatively, a timeline showing key player availabilities throughout a season.

## 4. Connecting Recruitment to On-Pitch Performance

*   **Direct Impact Analysis**: Select 2-3 key signings (one success, one failure, one debatable) and trace their pre-signing data, the rationale for their acquisition, their subsequent on-pitch performance metrics at United, and the team's performance in their area of influence before and after their arrival.
*   **Squad Gaps vs. Recruitment Actions**: Identify persistent on-pitch weaknesses (from Section 3) and evaluate whether recruitment has adequately addressed these gaps over recent transfer windows.

## 5. Supporting Analysis (Adjusted Depth - Concise Overview)

*   **5.1. Financial Context: Constraints and Enablers**
    *   Briefly discuss how the wage bill (wage-to-turnover ratio) and net transfer spend influence the club's ability to recruit desired profiles and how poor recruitment exacerbates financial pressures (e.g., high wages for underperformers, difficulty selling players).
*   **5.2. Operational Benchmarks: Data Infrastructure & Team**
    *   Succinctly compare Man Utd's data team size and analytics budget (as per `pasted_content.txt`) with competitors like Liverpool or Brighton. Focus on how this capacity (or lack thereof) directly impacts the sophistication of recruitment modeling and performance analysis.

## 6. Data-Driven Recommendations for Revival

*   **6.1. Revolutionizing Recruitment Strategy**:
    *   **Implement a Multi-Layered Data Model**: Suggest specific undervalued markets or leagues to target. Define key data-driven player profiles for priority positions.
    *   **Adopt "Moneyball" Metrics**: Propose specific metrics beyond G/A (e.g., xGChain, xGBuildup, pressure success rate, defensive duel win rate based on position) to identify talent that fits a specific tactical system.
    *   **Strengthen Youth Pipeline Integration**: Use data to identify internal talent ready for first-team opportunities, reducing reliance on expensive external signings.
*   **6.2. Optimizing On-Pitch Tactics through Performance Analytics**:
    *   **Tailor Tactics to Squad Strengths**: Based on current player metrics, suggest tactical tweaks (e.g., pressing intensity, build-up patterns, defensive line height) that could yield better results.
    *   **Player Development Plans**: Use performance data to create individualized development plans for players, focusing on areas of weakness identified by metrics.
*   **6.3. Investing in Analytics Capability**:
    *   Recommend specific roles to add to the data team (e.g., data scientists specializing in machine learning for recruitment, dedicated video analysts working with performance data).

## 7. Conclusion

*   **Summary of Findings**: Briefly reiterate the key issues identified in recruitment and on-pitch performance, supported by data insights.
*   **The Path Forward**: Emphasize that a cultural shift towards data-centric decision-making is crucial for Manchester United's return to sustained success.
*   **Value Proposition**: Conclude by stating how this analytical approach and the insights derived demonstrate the skills valuable to potential employers in the sports analytics field or data-driven organizations.

## 8. Data Sources & Tools (To be listed in the Notebook)

*   Acknowledge the primary data sources mentioned in `pasted_content.txt` (FBRef, Opta, Sofascore, Transfermarkt, Deloitte Reports) and any others hypothetically used for the analysis.
*   Mention Python (Pandas, Matplotlib, Seaborn, Scikit-learn if applicable for any modeling concepts) as the primary tool for analysis and visualization within the Jupyter Notebook.

---

# Reference Document Content Plan

## 1. Introduction

*   Purpose: To provide a comprehensive list of potential data sources, analytical tools, and further reading for conducting in-depth football analytics case studies, supporting the methodologies demonstrated in the Manchester United case study.

## 2. Data Sources

*   **2.1. Financial Data**
    *   Deloitte Football Money League
    *   Club Annual Financial Reports (e.g., Manchester United PLC Investor Relations)
    *   Company Registries (e.g., Companies House in the UK for club accounts)
    *   Forbes Football Rich List
*   **2.2. Player Performance & Match Statistics**
    *   FBRef.com (powered by StatsBomb)
    *   Opta (via official providers or derived stats on sites like WhoScored, SofaScore)
    *   SofaScore.com
    *   WhoScored.com
    *   Understat.com (for Expected Goals - xG data)
    *   Wyscout (professional scouting platform, some data may be public or cited)
*   **2.3. Transfer Market Data**
    *   Transfermarkt.co.uk (market values, transfer history, agent information)
    *   CIES Football Observatory (transfer values, player demographics)
*   **2.4. Tactical & Event Data (Advanced)**
    *   StatsBomb (open data and paid services)
    *   Metrica Sports (tracking and event data, some open data)
    *   Second Spectrum (official tracking provider for some leagues)
*   **2.5. Injury Data**
    *   PremierInjuries.com
    *   Transfermarkt (injury history per player)
    *   Academic research databases (PubMed, Google Scholar for studies on football injuries)
*   **2.6. Fan Sentiment & Social Media Data**
    *   Twitter API (requires developer account, potential costs)
    *   Reddit API (for forum discussions, e.g., r/soccer, r/reddevils)
    *   Google Trends (for tracking interest over time)

## 3. Analytical & Visualization Tools

*   **3.1. Programming Languages & Core Libraries**
    *   **Python**: 
        *   `pandas` (data manipulation and analysis)
        *   `numpy` (numerical computing)
        *   `scipy` (scientific computing)
        *   `scikit-learn` (machine learning)
        *   `statsmodels` (statistical modeling)
    *   **R**: 
        *   `dplyr`, `data.table` (data manipulation)
        *   `ggplot2` (visualization)
        *   `caret` (machine learning)
*   **3.2. Visualization Libraries (Python Focus)**
    *   `matplotlib` (foundational plotting)
    *   `seaborn` (statistical visualizations, built on Matplotlib)
    *   `plotly`, `bokeh` (interactive visualizations)
    *   `mplsoccer` (specialized library for football pitch visualizations)
*   **3.3. Business Intelligence & Dashboarding Tools**
    *   Tableau
    *   Microsoft Power BI
    *   Google Data Studio (Looker Studio)
    *   Qlik Sense
*   **3.4. Databases**
    *   SQL (PostgreSQL, MySQL, SQLite)
    *   NoSQL (MongoDB)
*   **3.5. Version Control & Collaboration**
    *   Git
    *   GitHub, GitLab

## 4. Further Reading & Resources

*   **Blogs & Websites**:
    *   StatsBomb Blog (statsbomb.com/blog)
    *   The Athletic (data-driven football articles)
    *   Spielverlagerung.com (tactical analysis, often data-informed)
    *   Friends of Tracking (YouTube channel and resources on tracking data)
    *   David Sumpter's Soccermatics Blog
*   **Books**:
    *   "Soccermatics" by David Sumpter
    *   "The Numbers Game: Why Everything You Know About Soccer Is Wrong" by Chris Anderson and David Sally
    *   "Football Hackers: The Science and Art of a Data Revolution" by Christoph Biermann
*   **Academic Journals & Conferences**:
    *   Journal of Sports Analytics
    *   MIT Sloan Sports Analytics Conference
    *   OptaPro Analytics Forum (formerly)


