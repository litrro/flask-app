import pytest
from app import app  # 引入你的 Flask 应用

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  # 提供一个测试客户端

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'  # 验证返回的数据
