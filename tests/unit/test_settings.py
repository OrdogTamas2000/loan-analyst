from loan_analyst.settings import Settings


def test_settings_reads_env(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@localhost:5432/loan_analyst")
    monkeypatch.setenv("SEC_USER_AGENT", "Test test@example.com")
    monkeypatch.setenv("API_KEYS", '["k1","k2"]')
    s = Settings()
    assert s.sec_user_agent == "Test test@example.com"
    assert s.api_keys == ["k1", "k2"]
