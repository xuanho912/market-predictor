from app.services.models.regime_models.base import RuleRegimeModel


recovery_model = RuleRegimeModel(name="recovery_model", up_bias=0.12, down_bias=-0.03, volatility_sensitivity=0.10)
