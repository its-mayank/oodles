from oodles.core.classes.anomalies.abstract_anomaly import AbstractAnomaly
from oodles.core.classes.anomalies.signal_manager import SignalManager


class EdgeCaseManager(AbstractAnomaly):
    def __init__(self, signal_formulae):
        super().__init__()
        self.signal_manager = SignalManager()
        self.signal_manager.add_signal_formulae(signal_formulae)

    def check(self, inputs, outputs, gts=None, extra_args={}):
        return

    def is_data_interesting(self, inputs, outputs, gts=None, extra_args={}):
        return self.signal_manager.evaluate_signal(
            inputs, outputs, gts=gts, extra_args=extra_args
        )

    def need_ground_truth(self):
        return False
