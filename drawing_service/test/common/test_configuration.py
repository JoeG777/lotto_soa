import pytest

from src.draw.common.configuration import Configuration

class TestConfiguration:

    @pytest.fixture
    def sample_configuration(self):
        return Configuration()
    
    @pytest.fixture
    def sample_configuration_with_env(self, monkeypatch):
        monkeypatch.setenv("DRAW_MESSAGE_BROKER_HOST", "hello")
        monkeypatch.setenv("DRAW_MESSAGE_BROKER_PORT", 1)
        return Configuration()

    def test_get_config_from_defaults(self, sample_configuration):
        
        assert sample_configuration.config_map.get("message_broker_host") == "localhost"
        assert sample_configuration.config_map.get("message_broker_port") == 5672

    def test_get_config_from_env(self, sample_configuration_with_env):
        
        assert sample_configuration_with_env.config_map.get("message_broker_host") == "hello"
        assert sample_configuration_with_env.config_map.get("message_broker_port") == str(1)