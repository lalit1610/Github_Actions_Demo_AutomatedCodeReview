def divide(a, b):
    """Divide two numbers - has a critical bug!"""
    return a / b  # BUG: No zero check!

def get_user_data(user_id):
    """Get user data from database - security vulnerability!"""
    query = "SELECT * FROM users WHERE id = " + str(user_id)  # SQL Injection!
    return execute_query(query)

def process_list(items):
    """Process list inefficiently"""
    result = []
    for i in range(len(items)):  # Inefficient iteration
        for j in range(len(items)):  # Unnecessary nested loop
            if i == j:
                result.append(items[i] * 2)
    return result

# Test code that will crash
if __name__ == "__main__":
    print(divide(10, 0))  # Division by zero!
    print(get_user_data("1; DROP TABLE users; --"))  # SQL injection attack!
