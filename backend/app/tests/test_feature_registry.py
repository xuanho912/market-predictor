import pytest

from app.services.feature_engineering.registry import FEATURE_TRANSFORMS, FeatureSpec


def test_required_transforms_are_registered() -> None:
    assert {"level", "change", "acceleration", "percentile", "cross_signal", "divergence"}.issubset(FEATURE_TRANSFORMS)


def test_feature_spec_rejects_unknown_transform() -> None:
    with pytest.raises(ValueError):
        FeatureSpec(
            name="price__spx__return__20d__raw",
            group="price",
            source="spx",
            frequency="daily",
            transform="raw",
            lag_policy="close_known",
            missing_value_policy="drop",
        )
