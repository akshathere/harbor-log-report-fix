Analyze the Apache access log in the working directory and extract traffic statistics.

To succeed, you must complete the following criteria:
1. Calculate the total number of requests.
2. Calculate the total number of unique client IP addresses.
3. Identify the most frequently requested page/path.
4. Save your findings as a valid JSON file exactly at `/app/report.json`.

The JSON must use these exact keys: `total_requests`, `unique_ips`, and `top_path`.