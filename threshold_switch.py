class ThresholdActivator(object):
    def __init__(self, activationThreshold, deactivationThreshold, mode=False):
        self.activationThreshold = activationThreshold
        self.deactivationThreshold = deactivationThreshold
        self.mode = mode
    def updateThreshold(self, currentValue):
        if currentValue >= self.activationThreshold:
            self.mode = True
        elif currentValue <= self.deactivationThreshold:
            self.mode = False