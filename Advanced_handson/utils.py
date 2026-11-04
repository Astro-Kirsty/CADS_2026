from gammapy.estimators import FluxPointsEstimator

def fake_and_run_flux_points_estimation(dataset_on_off, background, model_true):
    energy_axis = dataset_on_off.counts.geom.axes["energy"]
    ds = dataset_on_off.copy(name=dataset_on_off.name)
    ds.models = model_true
    ds.fake(background)
    fpe = FluxPointsEstimator(energy_edges=energy_axis.edges, 
                             selection_optional=["ul"], 
                             n_sigma_ul=2,
                             n_jobs=1    # Force n_jobs=1 to avoid multiprocessing in subprocess
                            )
    return fpe.run([ds])

    