# Course Highlights
---

## Module 1 · Python & Software Foundations Refresher 
**Goal**  
Refresh core Python and build professional coding habits that will never need “un-learning.”

| Step | Topic | Why It Matters |
|------|-------|---------------|
| 1 | **Data Types & Control Flow** | A quick sweep of syntax ensures later lessons don’t stall on basics. |
| 2 | **Functions & Docstrings** | Clear, reusable functions make every future project cleaner. |
| 3 | **Errors & Debugging** | Early comfort with exceptions saves hours of frustration later. |
| 4 | **OOP Essentials** | Classes/objects prepare the mind for real-world abstractions (e.g., “Trade,” “Strategy”). |
| 5 | **Project Hygiene** | Git, virtual envs, linting, and unit tests form habits that professionals rely on. |

---

## Module 2 · Statistics & Probability Refresher & Beyond
**Goal**  
Give intuitive command of data summaries, randomness, and basic inference.

| Step | Topic | Why It Matters |
|------|-------|---------------|
| 1 | **Descriptive Stats** | Understand “how big” and “how spread” before modeling. |
| 2 | **Correlation vs. Causation** | Shields against making false claims from patterns. |
| 3 | **Counting & Probability** | Foundation for thinking in chances, essential for risk. |
| 4 | **Sampling & CLT** | Explains why averages behave so nicely. |
| 5 | **Hypothesis Testing** | Basic yes/no decision-making with data. |
| 6 | **Intro Linear Regression** | First predictive tool; also links nicely into ML. |

---

## Module 3 · Data Wrangling & Time-Series Basics  
**Goal**  
Load, clean, reshape, and summarize real-world financial time series.

| Step | Topic | Why It Matters |
|------|-------|---------------|
| 1 | **NumPy Arrays** | Fast math “muscle” underneath pandas and ML libraries. |
| 2 | **Pandas DataFrames** | Industry-standard table tool; everything else plugs into it. |
| 3 | **Merging & Grouping** | Combine multiple files and summarize patterns quickly. |
| 4 | **Feature Engineering** | Rolling averages, lags, and indicators create signal out of raw price. |
| 5 | **Datetime Indexing** | Enables resampling (daily → weekly) and accurate joins. |
| 6 | **Stationarity & Volatility** | Core ideas before any forecasting or risk model. |
| 7 | **ARIMA (Conceptual)** | Shows where classical forecasting fits, without heavy math. |

---

## Module 4 · Machine Learning Fundamentals  
**Goal**  
Teach a **do-able** ML workflow—light on math, heavy on practical skill—so the student can build and critique simple models.

| Step | Topic | What to Achieve |
|------|-------|-----------------|
| 1 | **ML Mindset** | Difference between rules vs. data-driven models; importance of holding out test data. |
| 2 | **Data Preparation** | Train/validation/test splits, scaling numeric columns, one-hot encoding if needed. |
| 3 | **Baseline Regression** | Fit a single-feature linear model; read intercept & slope; check residual scatter. |
| 4 | **Multiple & Regularized Regression** | Add more inputs; introduce Ridge/Lasso as safeguards against “too many features.” |
| 5 | **Baseline Classification** | Logistic regression on a binary label (e.g., up vs. down day). |
| 6 | **Decision Trees** | Visual, intuitive method; acts as bridge to ensembles. |
| 7 | **k-Nearest Neighbors** | Simple non-parametric idea; contrasts with tree logic. |
| 8 | **Ensemble Snapshot** | Random Forest (bagging) and Gradient Boosting (boosting) for better accuracy without new math. |
| 9 | **Evaluation Metrics** | Regression → MSE & MAE; Classification → accuracy, precision, recall, F1, ROC-AUC. Emphasize “pick metric that matches goal.” |
|10 | **Model Tuning & Cross-Validation** | Grid search basics; why re-testing on unseen data is mandatory. |
|11 | **Interpretability** | Coefficient signs, feature importance bars; what drives predictions? |
|12 | **Mini-Project** | Student builds one regressor and one classifier on a small public set, writes a half-page reflection on results and pitfalls. |

---

## Module 5 · Async I/O in TypeScript  
**Goal**  
Create type-safe, non-blocking scripts for data collection and processing.

| Step | Topic | Why It Matters |
|------|-------|---------------|
| 1 | **TS Basics** | Strong typing catches bugs earlier. |
| 2 | **Promises & `async/await`** | Cleaner asynchronous flow than callbacks. |
| 3 | **Concurrent HTTP Fetching** | Pull market data for many symbols fast, within API limits. |
| 4 | **Async File Operations** | Save large responses without blocking. |
| 5 | **Streams & Memory Efficiency** | Handle big CSVs/logs in chunks. |

---

## Module 6 · Markets & Trading Fundamentals  
**Goal**  
Understand market mechanics and craft a back-testable indicator strategy.

| Step | Topic | Why It Matters |
|------|-------|---------------|
| 1 | **Market Plumbing** | Orders, tickers, OHLC—know the data you trade. |
| 2 | **Core Indicators** | SMA, EMA, RSI, MACD, Bollinger—standard trader vocabulary. |
| 3 | **Backtesting Workflow** | Simulate trade logic chronologically; avoid look-ahead bias. |
| 4 | **Performance Metrics** | Cumulative return, drawdown, Sharpe—quick health check. |
---

## Module 7 · Capstone Project  
**Project Components & Expectations:**

1. **Project Objective**  
   - Build an end-to-end trading algorithm that integrates:  
     1. Asynchronous data ingestion (Module 4)  
     2. Feature engineering (Module 3 and Module 5): compute technical indicators and any ML-driven signals  
     3. Simple model or rule-based signal generation (e.g., logistic regression on engineered features or pure indicator rules)  

2. **Data Ingestion & Preparation**  
   - Use a free financial API (e.g., Yahoo Finance via `yfinance` or Alpha Vantage)  
   - Asynchronously fetch OHLC data for a small basket of tickers (e.g., 3–5 symbols)  
   - Save cleaned data to disk in CSV or Parquet format  

3. **Feature Engineering**  
   - Compute at least three technical indicators (e.g., SMA_20, RSI_14, MACD) per ticker  
   - Construct lagged features (e.g., previous-day returns, rolling volatility)  
   - Optionally generate a simple ML-based signal:  
     - Train a basic classifier (logistic regression) on historical data to predict next-day price direction  
     - Evaluate model performance using precision, recall, accuracy, and AUC  

4. **Backtesting Engine**  
   - Implement a straightforward backtest loop:  
     - Iterate through each trading day in chronological order  
     - Generate buy/sell signals based on chosen rules or model outputs  
     - Simulate entry and exit, track portfolio equity after each trade  
     - Account for transaction cost as a fixed percentage (e.g., 0.1% per trade)  
     - Record trade-level metrics (entry date, exit date, P&L, return %)  

5. **Performance Analysis**  
   - Compute overall cumulative return and annualized return  
   - Calculate maximum drawdown:  
     - Define drawdown as `peak_equity – trough_equity` before a new peak  
     - Express as percentage of peak equity  
   - Compute Sharpe ratio:  
     - Use daily returns, subtract risk-free rate (assume 0% if unknown), divide by standard deviation of returns  
   - Plot equity curve over time (line chart) and drawdown curve (area or line below zero)  

6. **Reporting & Visualization**  
   - Create a concise Jupyter Notebook (or Python script with plots) that:  
     - Describes data sources and acquisition process  
     - Documents feature engineering steps with code snippets  
     - Shows backtesting pseudocode or actual loop with commentary  
     - Displays final performance charts: equity curve, drawdowns, distribution of returns (histogram)  
   - Write a brief summary (200–300 words) that highlights:  
     - Key findings (e.g., “Strategy returned X% with max drawdown Y% over Z years”)  
     - Limitations (e.g., data survivorship, no slippage modeling)  
     - Next steps for improvement (e.g., adding ML-driven signals, optimizing position sizing)  


---


## Appendix · Running the Course Day-to-Day

### 1 · Optimal 90-Minute Class Flow

| Segment | Mins | Purpose |
|---------|------|---------|
| **Warm-Up Quiz / HW disc.** | 10 | 3–5 rapid questions on last session; surfaces gaps early. |
| **Mini-Recap** | 5 | Highlight key take-aways from previous class; connects to today’s topic. |
| **Concept Drop** | 30 | Short lecture/demo of the new material. |
| **Guided Practice** | 30 | Code along or solve guided worksheet; instructor circulates or screenshares. |
| **Wrap-Up & Homework Brief** | 10 | Confirm what was built, assign concise homework, and post links to resources. |


---

### 2 · Assessment Strategy

| Type | When | Format | Weight |
|------|------|--------|--------|
| **Spot Checks** | Every class (warm-up quiz) | 3–5 MCQs or code-fill blanks | Ungraded, diagnostic |
| **Mini-Projects** | End of each module | Jupyter notebook or TS script + 150-word summary | 50 % |
| **Module Quizzes** | Every 5-8 classses | 15 min mixed theory/code prompts | 50 % |


**Grading Rubric Snapshot (Mini-Projects / Capstone)**
| Criterion | Points |
|-----------|--------|
| Correctness & Reproducibility | 40 |
| Clarity of Code & Comments | 20 |
| Insightful Interpretation of Results | 20 |
| Presentation / Report Quality | 20 |

---

### Quick-Look Dashboard

| Metric | Tool | How to Read |
|--------|------|------------|
| Commit frequency | GitHub Insights | Spiky? Student crams. Aim for steady daily commits. |
| Quiz average | Google Forms sheet | Trend ↑ = ready to accelerate; flat or ↓ = insert revision day. |
| Rubric scores (optional) | Notion database | Filter by “<70 % correctness” to find topics to reteach. |

---

## Appendix · How We Work: Assignments & GitHub

We use a professional Git workflow to manage all coding assignments. This process mirrors how software development teams collaborate. Your work will be submitted via **Pull Requests**, which is the standard way to propose changes to a codebase.

### **Your Assignment Workflow**

**I have protected the `main` branch.** This means you cannot push changes directly to it. You must work on a separate branch and open a Pull Request.

Here is the step-by-step process:

1.  **Accept & Clone the Assignment**:
    * Click the assignment link shared by me to create your private repository.
    * Clone it to your local machine:
        ```bash
        git clone <your-assignment-repo-url>
        cd <your-assignment-folder>
        ```

2.  **Set Up The Environment**:
    * Run this command **once** per assignment to create the virtual environment and install all dependencies.
        ```bash
        make install-dev
        ```

3.  **Create a New Branch**:
    * Before you start coding, create a new branch for your work. This keeps the `main` branch clean. Name it something descriptive.
        ```bash
        git checkout -b student/solution-feature
        ```
    * You are now on your new branch. Any changes you make will be on this branch only.

4.  **Code and Test**:
    * Activate the environment to use the installed tools:
        ```bash
        source .venv/bin/activate
        ```
    * Open `solution.py` and write your code.
    * As you work, check your solution by running the provided unit tests:
        ```bash
        make test
        ```
    * Your goal is to make all tests pass.

5.  **Commit and Push Your Branch**:
    * Once your tests are passing, commit your changes to your branch.
        ```bash
        git add .
        git commit -m "feat: Complete word frequency counter"
        ```
    * Now, push your *new branch* (not `main`) to GitHub. The `-u` flag sets it up to track the remote branch.
        ```bash
        git push -u origin student/solution-feature
        ```

6.  **Open a Pull Request (PR)**:
    * Go to your repository on GitHub. You will see a yellow banner with a button that says **"Compare & pull request"**. Click it.
    * The base repository should be your assignment, and the `base` branch should be `main`.
    * The `head` repository should be your fork, and the `compare` branch should be your `student/solution-feature` branch.
    * Give your PR a title (e.g., "Assignment 1 Submission") and a brief description.
    * Click **"Create pull request"**.

You have now successfully submitted your assignment! I can now review your code, leave comments, and merge it when it's approved.