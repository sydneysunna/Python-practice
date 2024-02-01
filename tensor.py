import torch

#x = torch.empty(3)
#print(x)
#returns a 1d vector with 3 elements

#x = torch.empty(2,3)
#print(x)
#returns a 2d vector with 2 rows and 3 columns and 6 elements

#x = torch.rand(2,2)
#print(x)
# returns a 2D vector with 4 random elements

#x = torch.ones(2,2)
#print(x)
# returns a 2D vector with 4 elements with the value 1

#x = torch.ones(2,2)
#print(x.dtype)
#by default, torch returns floats

#x = torch.ones(2,2, dtype=torch.int)
#x = torch.ones(2,2, dtype=torch.double)
#x = torch.ones(2,2, dtype=torch.float16)
#print(x.dtype)

#x = torch.tensor([2.5,0.2])
#print(x)
#create a tensor of specific values

#x = torch.rand(1,1)
#y = torch.rand(1,1)
#z=x+y
#print(z)
