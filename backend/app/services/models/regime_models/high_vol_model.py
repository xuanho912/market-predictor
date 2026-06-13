from app.services.models.regime_models.base import RuleRegimeModel


high_vol_model = RuleRegimeModel(name="high_vol_model", up_bias=-0.02, down_bias=0.10, volatility_sensitivity=0.20)
