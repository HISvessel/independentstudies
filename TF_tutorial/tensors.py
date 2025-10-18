import torch

x = torch.tensor([1., 2., 3., 4.])
print(f'1D object from torch tensor: {x}')

tz = torch.zeros((3, 3))
print(f'2d tensor: {tz}')