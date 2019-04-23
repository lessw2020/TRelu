#import torch.nn.functional as F  #likely you don't need but just in case, uncomment

class TRelu(nn.Module):
    def __init__(self, threshold= - .25, mean_shift=-.03):
        super().__init__()
        self.threshold = threshold
        self.mean_shift = mean_shift
    
    def forward(self,x):
        x = F.relu(x)+self.threshold
        
        if self.mean_shift is not None:
            x.sub_(self.mean_shift)
            
        return x