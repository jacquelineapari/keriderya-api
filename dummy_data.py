# add dummy data
from app import db  # Import SQLAlchemy database instance
from app.models import YourModel  # Replace YourModel with the actual model name

# Creating dummy data
dummy_data = YourModel(name="John Doe", email="john.doe@example.com")  # Adjust fields and data as needed

# Adding the data to the session
db.session.add(dummy_data)

# Committing to the database
db.session.commit()

print("Dummy data added successfully.")
