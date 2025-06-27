

def test_sentiment_api_positive(test_client):
    payload = {"text": "FastAPI is amazing!"}
    response = test_client.post("/nlp/sentiment", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "score" in data
    assert data["label"] in ["POSITIVE", "NEGATIVE"]

def test_sentiment_api_invalid_input(test_client):
    payload = {"text": ""}
    response = test_client.post("/nlp/sentiment", json=payload)

    assert response.status_code == 422 or response.status_code == 500
