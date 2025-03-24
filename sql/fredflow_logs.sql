CREATE TABLE fredflow_logs (
    log_id SERIAL PRIMARY KEY,
    fred_series TEXT NOT NULL,
    row_tally INT NOT NULL,
    start_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stop_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
