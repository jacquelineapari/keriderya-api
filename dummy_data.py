from app import db  # Import SQLAlchemy database instance
from app.models.menu_model import MenuModel  # Import the MenuModel

# Creating dummy data for the MenuModel
menu_item = MenuModel(
    name="Sample Menu Item",  # Adjust fields and data as needed
    price=1000,
    description="A delicious sample dish.",
    availability=True,
    restaurant_id=1,  # Assuming a restaurant with ID 1 exists
    category_id=1  # Assuming a category with ID 1 exists
)

# Adding the data to the session
db.session.add(menu_item)

# Committing to the database
db.session.commit()

print("Dummy data added successfully.")
