import torch
import torch.nn.functional as F

# Simulated input (3 words, 4 embedding dimensions)
Q = torch.rand((3, 4))
K = torch.rand((3, 4))
V = torch.rand((3, 4))

# Compute attention scores (Q @ K^T)
attention_scores = Q @ K.T  

# Normalize using Softmax
attention_weights = F.softmax(attention_scores, dim=-1)

# Compute final attention output
output = attention_weights @ V  

print("Attention Weights:\n", attention_weights)
print("\nSelf-Attention Output:\n", output)
