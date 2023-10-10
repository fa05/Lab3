import db # Import the functions defined in database.py

# Create the database and table
db.create_db_table()

# Insert a user (you can repeat this for multiple users)
user = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "phone": "1234567890",
    "address": "123 Main St",
    "country": "USA"
}
inserted_user = db.insert_user(user)
print("Inserted User:", inserted_user)

# Fetch all users and print them
users = db.get_users()
print("All Users:")
for user in users:
    print(user)

# Fetch a user by ID (replace '1' with an actual user ID)
user_id = 1
user = db.get_user_by_id(user_id)
print("User by ID:", user)

# Update a user's information (replace '1' with an actual user ID)
user_id_to_update = 1
updated_user_data = {
    "user_id": user_id_to_update,
    "name": "Updated Name",
    "email": "updated_email@gmail.com",
    "phone": "9876543210",
    "address": "456 Updated St",
    "country": "Canada"
}
updated_user = db.update_user(updated_user_data)
print("Updated User:", updated_user)

# Delete a user by ID (replace '1' with an actual user ID)
user_id_to_delete = 1
delete_result = db.delete_user(user_id_to_delete)
print(delete_result)
