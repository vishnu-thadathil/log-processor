# Test Cases

## Test Case 1: Valid Log Entries
**Input:**
{
    "candidate_id": "12345",
    "log_content": "[2024-01-07 10:15:30] ERROR: Database connection failed\n[2024-01-07 10:15:35] INFO: Retry attempt 1"
}
**Expected Output:**
{
    "statusCode": 200,
    "body": {
        "candidate_id": "12345",
        "result": {
            "total_errors": 1,
            "unique_error_messages": ["Database connection failed"]
        }
    }
}

## Test Case 2: Empty Log
**Input:**
{
    "candidate_id": "12345",
    "log_content": ""
}
**Expected Output:**
{
    "statusCode": 200,
    "body": {
        "candidate_id": "12345",
        "result": {
            "total_errors": 0,
            "unique_error_messages": []
        }
    }
}

## Test Case 3: Malformed Log Entry
**Input:**
{
    "candidate_id": "12345",
    "log_content": "[2024-01-07 10:15:30] ERROR Database connection failed"
}
**Expected Output:**
{
    "statusCode": 200,
    "body": {
        "candidate_id": "12345",
        "result": {
            "total_errors": 0,
            "unique_error_messages": []
        }
    }
}
