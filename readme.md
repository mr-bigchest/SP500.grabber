# SP500.grabber
This is a personal project that aims to refurbish a rudimentary script I made in college that webscraped stock information about the portfolio of the Finance Club I was in. It was split into two files and existed for pure function; it also had a lot of techniques that I have since learned not to do. The purpose of this file is to provide (via GUI) a tool for any user to collect pertinent financial information regarding their portfolio, a sector of the financial market, or more detailed information on a specific company (e.g. 10-K & 10-Q analysis).

I have uploaded the original webscraping component as a scarlet letter that will propel me to display the skillset growth I feel I have experienced since the inception of this document. I intend for this project ot undergo consistent iteration. Furthermore, I hope that once a polished version of this project exists, I can share it with my old finance club to save them the sisyphean task of financial statement analysis in Excel. 

# Current List of Intended Functions: (Subject to Change)
  - Provide Graphical User Interface (increases accessibility for non-Python users)
  - Get current day information on any stock or stocks listed in the S&P 500 (may expand for NASDAQ, DJIA)
  - Collect historical information on any stock or stocks listed in the S&P 500 (also may expand for NASDAQ, DJIA)
  - Perform basic financial calculations on portfolio returns. Adjustable from total portfolio to asset classes & custom subcategories
  - Collect 10-K and 10-Q documents for S&P 500 stocks
  - Convert collected financial statement data into actionable financial information through a variety of financial calculations: 
      - Activity Ratios, Liquidity Ratios, Solvency Ratios, Profitability Ratios, & DuPont Analysis
      - Basic growth rate calculations and statistics
      - Gordon & Multistage DDM
      - Basic DCF Valuations
      - Basic FCFE & FCFF
      - Vertical & Horizontal Analysis
      - Multiples Ratios calculations (P/E, P/BV, etc.)
  - Provide the user a capability to export any of their collected information to Excel, CSV
  - Provide basic explanations for what different financial calculations mean and how the information can be actionable
  - In lieu of user account system, upload data created from previous sessions to get going again (user accounts possible but fact finding required)
 
# Current Capabilities:
  - Get current day information on any stock or stocks listed in the S&P 500

# GUI Layout [WIP]:
  - https://www.figma.com/file/5v2WxP29Gf11b0lUHBYDNj/grabber-dash?node-id=0%3A1
 
# Under Construction: 
  - Rudimentary GUI
  - Re-work code of primary functions to remove any global variables / general inefficiencies
  - System design documentation
  
 # Next in Line:
  - Portfolio return calculations
  - customizable subcategory returns
  - 10-K & 10-Q data collection

# Future Considerations
  - Establish central database to avoid constant recalculation and data collection.
  - More robust growth rate calculations. It will need to take the art component of finance into account and be flexible enough to handle user toggles beyond basic RoE * Retention Ratio
  - Rudimentary competitor analysis. But will likely be a later feature as establishing the capability with any real function has many prerequisites
