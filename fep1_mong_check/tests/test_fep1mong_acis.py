from ..fep1_mong_check import model_path, FEP1MongCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest

fep1mong_rt = RegressionTester(FEP1MongCheck, model_path, "fep1_mong_test_spec.json")

# ACIS state builder tests

fep1mong_rt.run_models(state_builder='acis')

# Prediction tests


@pytest.mark.parametrize('load', all_loads)
def test_prediction(answer_store, load):
    fep1mong_rt.run_test("prediction", load, answer_store=answer_store)

# Validation tests


@pytest.mark.parametrize('load', all_loads)
def test_validation(answer_store, load):
    fep1mong_rt.run_test("validation", load, answer_store=answer_store)
