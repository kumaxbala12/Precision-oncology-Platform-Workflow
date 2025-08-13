
def test_smoke_imports():
    import modules.bulk_rnaseq.train_classifier as m1
    import modules.drug_response.train_elasticnet as m2
    import modules.survival.cox_pipeline as m3
    import modules.multiomics.integrate_cca as m4
    assert True
