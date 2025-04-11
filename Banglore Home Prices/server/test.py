# In your server.py or somewhere in the application startup
import util

try:
    util.load_saved_artifacts()
    print("Artifacts loaded successfully.")
except Exception as e:
    print(f"Error loading artifacts: {e}")
