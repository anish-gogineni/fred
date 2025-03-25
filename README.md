# FRED ETL Pipeline  

This repository contains a Python-based ETL pipeline for fetching economic data from the **Federal Reserve Economic Data (FRED) API**, transforming it, and loading it into a **PostgreSQL** database. The process also logs each data load operation in a dedicated `fredflow_logs` table.  

## 🚀 Features  
- **Automated Data Extraction:** Fetches economic indicators from the FRED API.  
- **Data Transformation:** Converts raw data into a structured format suitable for storage.  
- **Upsert Process:** Ensures efficient data loading and prevents duplication.  
- **Logging Mechanism:** Records each ETL operation in the `fredflow_logs` table.  

## 📂 Folder Structure  
```plain text
fred/ 
│── sql/
|   │── create_tables.sql
|   │── create_fredflow_logs.sql
│── extract.py
│── transform.py
│── load.py
│── main.py
│── example_config.py 
│── requirements.txt
│── .gitignore
```


## 🛠️ Setup and Configuration  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/anish-gogineni/fred.git
cd fred
```

### **2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)**
```sh
conda create --name myenv python=3.x
conda activate myenv
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure API and Database Connection**

1. Create a config.py file by copying the example config:
```sh
cp example_config.py config.py
```

2. Edit config.py and update the following details:
```py
FRED_API_KEY = "your_fred_api_key"

DB_CONFIG = {
    "dbname": "your_db_name",
    "user": "your_db_username",
    "password": "your_db_password",
    "host": "your_db_host",
    "port": "5432"
}

# List of FRED series to be fetched
# Dictionary mapping FRED series to database table names
FRED_SERIES_MAPPING = {
    "GDP": "GDP",   # Gross Domestic Product
    "UNRATE": "UNRATE", # Unemployment Rate
    "DFF": "DFF",  # Effective Federal Funds Rate,
    "CPIENGSL": "CPIENGSL",  # Energy in US City Average
    "GFDEBTN": "GFDEBTN",  # Total Public Debt	
    "CORESTICKM159SFRBATL": "CORESTICKM159SFRBATL"  # Sticky CPI
}
```

3. Ensure config.py is ignored by Git (already handled in .gitignore).


### **5️⃣ Set Up the Database**
Create tables if you haven't created the tables yet, run the sql commands present in the sql folder in PostgreSQL.


### **▶️ Running the ETL Pipeline**
Simply execute main.py to fetch, transform, and load data for all configured FRED series:
```sh
python main.py
```

