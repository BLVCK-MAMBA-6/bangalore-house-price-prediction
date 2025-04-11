import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

# Function to get the estimated price based on input parameters
def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Check if location exists in the list of locations
        if location.lower() not in __locations:
            raise ValueError(f"Location '{location}' not found in the model.")

        # Locate index for the given location
        loc_index = __locations.index(location.lower())

        # Prepare feature vector (ensure the order of features is consistent with what was used during training)
        x = np.zeros(len(__data_columns))
        x[0] = sqft  # sqft feature
        x[1] = bath  # bath feature
        x[2] = bhk  # bhk feature
        if loc_index >= 0:
            x[loc_index + 3] = 1  # Set 1 for the location index (location starts from index 3 in the model)

        # Return the predicted pricess
        return round(__model.predict([x])[0], 2)

    except Exception as e:
        return str(e)


# Function to get location names
def get_location_names():
    if __locations is None:
        load_saved_artifacts()  # Ensure artifacts are loaded if not already
    return __locations

# Load saved model and artifacts
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    # Load columns.json to extract location names
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]  # Locations are stored from index 3 onward

    # Load the pre-trained model
    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

# Ensure artifacts are loaded when the script runs directly
if __name__ == "__main__":
    load_saved_artifacts()  # Load saved artifacts when running the script directly
    print(get_location_names())  # Print location names to verify
    print(get_estimated_price('location_1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('location_1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('location_ambalipura', 1000, 2, 2))
    print(get_estimated_price('location_ambedkar nagar', 1000, 2, 2))
