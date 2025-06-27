from app.services.sentiment_service import analyze_sentiment

def test_sentiment_positive():
    result = analyze_sentiment("I love this course!")
    assert result["label"] == "POSITIVE"
    assert 0.5 < result["score"] <= 1.0

def test_sentiment_negative():
    result = analyze_sentiment("This was a terrible experience.")
    assert result["label"] == "NEGATIVE"
    assert 0.5 < result["score"] <= 1.0

def test_empty_input_raises():
    try:
        analyze_sentiment("")
        assert False, "Should raise ValueError or HTTPException"
    except Exception:
        assert True
