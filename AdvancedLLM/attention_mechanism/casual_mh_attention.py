import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.heads = heads
        self.head_dim = embed_size // heads

        # Linear layers for Q, K, V
        self.W_q = nn.Linear(embed_size, embed_size)
        self.W_k = nn.Linear(embed_size, embed_size)
        self.W_v = nn.Linear(embed_size, embed_size)

        # Final output linear layer
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, X, mask=None):
        batch_size, seq_length, embed_size = X.shape

        # Compute Q, K, V
        Q, K, V = self.W_q(X), self.W_k(X), self.W_v(X)

        # Split into multiple heads and reshape
        Q = Q.view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)

        # Compute attention scores
        attention_scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)

        # Apply causal mask (if provided)
        if mask is not None:
            attention_scores = attention_scores.masked_fill(mask == 0, float("-inf"))

        # Compute attention weights with softmax
        attention_weights = F.softmax(attention_scores, dim=-1)

        # Apply attention to values
        out = torch.matmul(attention_weights, V)

        # Merge heads and pass through output layer
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_length, embed_size)
        out = self.fc_out(out)

        return out

# Example input (batch_size=1, seq_length=5, embed_size=8)
seq_length = 5
embed_size = 8
heads = 2

X = torch.rand((1, seq_length, embed_size))

# Create causal mask (lower triangular matrix)
mask = torch.tril(torch.ones((seq_length, seq_length))).unsqueeze(0).unsqueeze(0)

# Initialize attention layer and apply it with the mask
attention_layer = MultiHeadAttention(embed_size=embed_size, heads=heads)
output = attention_layer(X, mask=mask)

print("Causal Mask:\n", mask)
print("\nMulti-Head Attention Output with Causal Mask:\n", output)
