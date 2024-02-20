import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    input_payload = event['input_payload']
    # Log start of processing
    logger.info("Starting ProcessInput Lambda function.")
    # Perform initial processing
    processed_data = input_payload.upper()
    return {
        'processed_data': processed_data
    }


def process_handler(event, context):
    processed_data = event['processed_data']
    # Log validation results
    logger.info("Starting ValidatePayload Lambda function.")

    # Example: Validate payload (replace with your validation logic)
    if processed_data.isupper():
        validation_result = "Valid"
    else:
        validation_result = "Invalid"
    return {
        'validation_result': validation_result
    }


def validate_handler(event, context):
    validation_result = event['validation_result']
    # Log processing steps
    logger.info("Starting ProcessData Lambda function.")
    # Example: Perform main processing based on validation result
    if validation_result == "Valid":
        result = "Processing successful"
    else:
        result = "Processing failed"
    return {
        'result': result
    }
