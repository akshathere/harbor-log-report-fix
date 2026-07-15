import json
from pathlib import Path

def test_report_validity():
    """The report exists, is valid JSON, and contains the real outcome."""
    report_path = Path("/app/report.json")
    
    # 1. Check existence
    assert report_path.exists(), "report.json not found in /app/"
    
    # 2. Check JSON parsing
    with open(report_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            assert False, "report.json is not a valid JSON file"
            
    # 3. Check for the required keys (Real Outcome)
    assert "total_requests" in data, "Missing 'total_requests' key in JSON"
    assert "unique_ips" in data, "Missing 'unique_ips' key in JSON"
    assert "top_path" in data, "Missing 'top_path' key in JSON"
    
    # Ensure they aren't just empty strings/nulls
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert isinstance(data["top_path"], str), "top_path must be a string"