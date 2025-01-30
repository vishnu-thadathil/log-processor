import json
import re

def process_log_file(log_content: str) -> dict[str, object]:
    """Extracts error patterns from log files.
    
    Args:
        log_content (str): Log file content as a string.
    
    Returns:
        dict[str, object]: Dictionary with total error count and unique error messages.
    """

    try:
        # Check if input is a string
        if not isinstance(log_content, str):
            raise ValueError("Input must be a string")
        
        # Regular expression to match ERROR log entries
        error_pattern = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ERROR: (.+)')
        errors = error_pattern.findall(log_content)
        
        # Return the result
        return {
            'total_errors': len(errors),
            'unique_error_messages': sorted(set(errors))
        }
    except Exception as e:
        # Handle errors and return a default response
        return {
            'total_errors': 0,
            'unique_error_messages': [],
            'error': f'Error processing log: {str(e)}'
        }

def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """

    try:
        # Extract candidate_id and log_content from the event
        candidate_id = event.get("candidate_id", "Unknown")
        log_content = event.get("log_content", "")
        
        # Process the log content
        result = process_log_file(log_content)
        
        # Return the expected response
        return {
            "statusCode": 200,
            "body": {
                "candidate_id": candidate_id,
                "result": result
            }
        }
    except Exception as e:
        # Handle unexpected errors
        return {
            "statusCode": 500,
            "body": {
                "candidate_id": event.get("candidate_id", "Unknown"),
                "error": f"Internal Server Error: {str(e)}"
            }
        }
