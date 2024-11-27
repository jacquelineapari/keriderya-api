from app import db  # Import SQLAlchemy database instance
from app.models.menu_model import MenuModel  # Import the correct model

# Creating dummy data for the menu model
dummy_data = MenuModel(
    name="Cheeseburger",  # Adjust fields and data as needed
    price=200,
    description="A delicious cheeseburger with all the fixings.",
    availability=True,
    restaurant_id=1,  # Use an appropriate restaurant_id
    category_id=1,    # Use an appropriate category_id
)

# Adding the data to the session
db.session.add(dummy_data)

# Committing to the database
db.session.commit()

print("Dummy data added successfully.")
