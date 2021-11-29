#!/usr/bin/env python
# coding: utf-8
from evidently.tabs.base_tab import Tab, Verbose
from evidently.widgets.cat_output_drift_widget import CatOutputDriftWidget
from evidently.widgets.cat_target_pred_feature_table_widget import CatTargetPredFeatureTable


class CatTargetDriftTab(Tab):
    widgets = [
        (CatOutputDriftWidget("Target Drift"), Verbose.ALWAYS),
        (CatOutputDriftWidget("Prediction Drift", 'prediction'), Verbose.ALWAYS),
        (CatTargetPredFeatureTable("Target (Prediction) Behavior By Feature"), Verbose.ALWAYS),
    ]
