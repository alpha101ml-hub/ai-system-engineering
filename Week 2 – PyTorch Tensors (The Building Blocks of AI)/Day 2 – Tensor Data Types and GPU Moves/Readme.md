## Week 2 – Day 2
- Learned tensor data types (`dtype`): float32, float16, int32, etc.
- Converted between dtypes using `.to(dtype)`
- Checked for GPU availability with `torch.cuda.is_available()`
- Moved tensors between CPU and GPU using `.to('cuda')` and `.to('cpu')`
- Compared CPU vs GPU speed on matrix multiplication
- **Key insight:** GPUs are massively faster for large tensor math –
- but you must explicitly move data there

### What is torch.randn vs torch.rand ?
- The core difference is that torch.rand samples numbers from a uniform distribution, 
- while torch.randn samples numbers from a standard normal (Gaussian) distribution

### What is matrix multiplication ?
- Matrix multiplication is a mathematical operation
- that multiplies two matrices to produce a single new matrix

### What is CUDA ?
- CUDA (Compute Unified Device Architecture) is a parallel computing platform
- and programming model created by NVIDIA
