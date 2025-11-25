import requests

def test_create_user():
    # Use a simple public test API that returns 201
    res = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "QA Engineer"}
    )
    assert res.status_code == 201
