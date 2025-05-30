# drug_optimization/gnn_model.py

import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class DrugGNN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(DrugGNN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, training=self.training, p=0.3)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)
