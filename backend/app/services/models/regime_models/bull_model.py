from app.services.models.regime_models.base import RuleRegimeModel


bull_model = RuleRegimeModel(name="bull_model", up_bias=0.16, down_bias=-0.08, volatility_sensitivity=0.08)
