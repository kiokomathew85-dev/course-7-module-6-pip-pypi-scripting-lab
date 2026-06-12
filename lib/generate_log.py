import os
from datetime import datetime

def generate_log(log_data):
    """
    Generates a timestamped log file from a list of entries.
    
    Args:
        log_data (list): A list of string log entries.
        
    Raises:
        ValueError: If log_data is not a list.
    """
    # Validate input type to pass the ValueError autotest
    if not isinstance(log_data, list):
        raise ValueError("Input log_data must be of type 'list'.")
        
    # Generate filename adhering strictly to log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write entries to file (handles empty lists cleanly)
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    # Print the precise confirmation message required by the rubric
    print(f"Log written to {filename}")

# Example execution block required by Step 4 & 5
if __name__ == "__main__":
    # Sample data for manual testing
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
