import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold


def relative_importance(df, target, features, drop_features_with_nulls=True, drop_invariant_features=True,
                        invariance_threshold=0.03, verbose=False):
    _df = df.copy()
    _features = features.copy()
    print(_df.shape)
    if verbose:
        print(f"Dataset size before dropping nulls --> {_df.shape}")
    # drop if there are any nulls in the target
    _df = _df.dropna(subset=[target])
    if verbose:
        print(f"Dataset size after dropping nulls --> {_df.shape}")
    # drop features with null data
    if drop_features_with_nulls:
        # check for features with null data
        features_with_null_data = (
            _df[_features]
                .columns[_df[_features].isna().any()]
                .tolist()
        )
        if len(features_with_null_data) > 0 and verbose:
            print(
                f'{" ,".join(features_with_null_data)} will be ignored to compute RW due to the presence of nulls'
            )
        _features = [col for col in _features if col not in features_with_null_data]

    if drop_invariant_features:
        feat_selector = VarianceThreshold(threshold=invariance_threshold)
        try:
            feat_selector.fit(_df[_features])
        except ValueError as ve:
            print(ve)
        invariant_features = [
            feat
            for feat, var in zip(_features, feat_selector.variances_)
            if var <= invariance_threshold
        ]
        if verbose and len(invariant_features) > 0:
            print(
                f'{" ,".join(invariant_features)} will be ignored to compute RW due to invariance'
            )
        # exclude the invariant features
        _features = [col for col in _features if col not in invariant_features]
    all_features = _features.copy()
    all_features.insert(0, target)
    corr_all = _df[all_features].apply(pd.to_numeric, errors="coerce").corr()
    corr_xx = corr_all.iloc[1:, 1:].copy()
    corr_yy = corr_all.iloc[1:, 0].copy()
    w_corr_xx, v_corr_xx = np.linalg.eig(corr_xx)
    num_x = len(corr_xx)
    idx_diag = np.diag_indices(num_x)
    diag = np.zeros((num_x, num_x), float)
    diag[idx_diag] = w_corr_xx
    delta = np.sqrt(diag)
    coef_xz = v_corr_xx @ delta @ v_corr_xx.transpose()
    coef_yz = np.linalg.inv(coef_xz) @ corr_yy
    rsquare = sum(np.square(coef_yz))
    if verbose:
        print(f"r2 score --> {rsquare}")
    raw_weights = np.square(coef_xz) @ np.square(coef_yz)
    normalized_weights = (raw_weights / rsquare) * 100
    rw_df = pd.DataFrame(
        data={
            "feature": _features,
            "raw_rel_imp": raw_weights,
            "norm_rel_imp": normalized_weights,
        }
    )
    rw_df.sort_values(["raw_rel_imp"], ascending=False, inplace=True)
    return rw_df
