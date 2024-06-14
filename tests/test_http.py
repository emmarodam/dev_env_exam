import os
import http.client

def test_get_coffee_beans():
    host = 'localhost'
    port = 8000

    # Setting up environment
    os.environ['POSTGRES_DB'] = 'test_db'
    os.environ['POSTGRES_USER'] = 'test_user'
    os.environ['POSTGRES_PASSWORD'] = 'test_password'

    # Send GET request to server
    conn = http.client.HTTPConnection(host, port)
    conn.request('GET', '/')
    response = conn.getrespose()

    # Check response = 200
    if response.status != 200:
        print(f"Error: Unexpected status code - {response.status}")
        return

    # Expected data
    expected_data = """Coffee Bean ID: 1, Name: Arabica, Description: Arabica beans are known for their smooth and mild flavor profile with subtle acidity. They often have floral and fruity notes, making them popular for specialty coffees., Price: 20 Coffee Bean ID: 2, Name: Robusta, Description: Robusta beans have a stronger, more robust flavor compared to Arabica beans. They are often higher in caffeine content and have a more bitter taste with earthy and woody notes., Price: 15 Coffee Bean ID: 3, Name: Ethiopian Yirgacheffe, Description: These beans are known for their bright acidity, floral aroma, and fruity flavor notes. Ethiopian Yirgacheffe is prized for its complex and vibrant taste profile., Price: 25"""

    # Read and decode response data
    response_data = response.read().decode('uft-8')
    for expected_line in expected_data:
        if expected_line not in response_data:
            print(f"Error: Expected data not found in response - {expected_line}")
            return

    print("Expected data: ")
    print(expected_data)
    print("Actual data: ")
    print(response_data)
    print("Test passed: GET request successful")

    conn.close()

if __name__ == '__main__' :
    test_get_coffee_beans()

