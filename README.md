# Log Processor - AWS Lambda Deployment

This repository contains the Python implementation of a log processor function designed to analyze log files and extract error patterns. The function is intended to be deployed as an AWS Lambda and exposed via API Gateway.

## Features
- Extracts error messages from log entries.
- Handles edge cases such as empty logs and malformed entries.
- Returns the total count of errors and a list of unique error messages.

## Setup
1. Clone this repository:
   ```git clone https://github.com/vishnu-thadathil/log-processor.git```
2. Navigate to the project directory:
    ```cd log-processor```

## Deployment Instructions
Refer to the `DEPLOYMENT.md` file for detailed steps on deploying the function to AWS Lambda and setting up API Gateway.

## Test Cases
Refer to the `TEST_CASES.md` file for a list of test cases used to validate the functionality.

## Additional Documentation

### Known Limitations
1. The function assumes well-formed log entries. Malformed entries may not be processed correctly.
2. Performance may degrade for very large log files due to line-by-line processing.
3. AWS Lambda constraints (e.g., 15-minute execution time) may limit the function's ability to process extremely large logs.

### Improvement Suggestions
1. Add robust input validation and detailed error messages.
2. Optimize performance using streaming and parallel processing.
3. Integrate with AWS services like S3 and Step Functions for advanced workflows.
4. Enhance error handling and logging for better monitoring.

### Scaling Considerations
1. Use Amazon S3 for storing and processing large log files.
2. Optimize memory and timeout settings to reduce costs.
