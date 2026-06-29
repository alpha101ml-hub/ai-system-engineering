'''
Day 2 - Tensor Data Types and GPU Moves

Goal: Learn how to check and change tensor data types, detect if you have a GPU, move tensors between CPU and GPU, and understand why it matters.
'''

'''
In python, numbers can be intergers (int), floating point (float), etc. In PyTorch tensors also have types. Common ones:


dtype - torch.float32 (default)	Description - 32-bit floating point  	Memory Usage - 4 bytes per number

dtype - torch.float64   Description - 64-bit floating point (double)	Memory Usage - 8 bytes per number

dtype - torch.int32  Description - 32-bit integer	
Memory Usage - 4 bytes per number

dtype - torch.int64	 Description - 64-bit integer (default for ints)	Memory Usage - 8 bytes per number

dtype - torch.float16  Description -16-bit floating point (half precision)	Memory Usage - 2 bytes per number


Why this matters for AI:
Using smaller dytpes (like floats16) can halve memory usage and speed up computation, especially on newer GPUs. But sometimes you lose precision - it's a trade-off.
'''

import torch

print("--- DATA TYPES (DTYPES) ---")

# Create a tensor with default (float32)
x = torch.tensor([1,2,3])
print("Default dtypes:", x.dtype)

# Create a tensor with specific dtype
x_int = torch.tensor([1,2,3], dtype = torch.int32)
print("int32 tensor:", x_int)
print("int32 dtype:", x_int.dtype)

x_float64 = torch.tensor([1.0,2.0,3.0], dtype=torch.float64)
print("float64 tensor:", x_float64)
print("float64 dtype:", x_float64.dtype)

# Convert existing tensor toa another dytpe
x = torch.tensor([1.5, 2.7, 3.2])
print("\nOriginal tensor:", x)
print("original tensor:", x.dtype)

x_int = x.to(torch.int32) # Convert to int32(truncates decimals)
print("Converted to int32:", x_int)
print("New dtype:", x_int.dtype)

x_half = x.to(torch.float16)
print("Converted to float16:", x_half)
print("New dtype:", x_half.dtype)

'''
PyTorch can use NVIDIA GPUs via CUDA. Let's check if your system has one.
'''

print("\n--- GPU CHECK ---")

# Check if CUDA (GPU) is available
if torch.cuda.is_available():
    print("✅ GPU is available!")
    print("GPU name:", torch.cuda.get_device_name(0))
    print("Number of GPUs:", torch.cuda.device_count())
else:
    print("❌ GPU not available - using CPU only.")
    
'''
If you don't have an NVIDIA GPU or CUDA installed, this will print the "not available" message. That's fine - everything still works on CPU.
'''

'''
Tensors can be created on CPU (default) or explicitly on GPU (if available)
'''

print("/n--- CREATING TENSORS ON CPU AND GPU ---")

# CPUU tensor (default)
cpu_tensor = torch.tensor([1,2,3])
print("CPU tensor device: ", cpu_tensor.device)

# IF GPU is available, create a tensor directly in GPU
if torch.cuda.is_available():
    gpu_tensor = torch.tensor([4,5,6], device = 'cuda')
    print("GPU tensor devide:", gpu_tensor.device)
else:
    print("Skipping GPU tensor creation - no GPU.")
    

'''
device='cuda' tells PyTorch to create the tensor on the GPU.
'''

'''
You can move existing tensors with .to(devive) or .cuda() / .cpu()
'''

print("\n--- MOVING TENSORS ---")

# Start with a CPU tensor
x_cpu = torch.tensor([10,20,30])
print("Original (CPU):", x_cpu)
print("Device:", x_cpu.device)

# Move to GPU if available
if torch.cuda.is_available():
    x_gpu = x_cpu.to('cuda')  # or x_cpu.cuda()
    print("Moved to GPU:", x_gpu)
    print("Device after move:", x_gpu.device)

    # Move back to CPU
    x_back_cpu = x_gpu.to('cpu')  # or x_gpu.cpu()
    print("Moved back to CPU:", x_back_cpu)
    print("Device after back:", x_back_cpu.device)
else:
    print("No GPU to move to - staying on CPU.")
    
    
''''
Let's see the speed difference with a large tensor operations.
'''

print("/n--- CPU vs GPU SPEED TEST")

import time

# Create a large tensor (1000 x 1000)
size = 1000
print(f"Performing matrix multiplication on {size}x{size} tensors...")

# CPU test
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
result_cpu = a_cpu @ b_cpu # Matrix multiplication
if torch.cuda.is_available():
    torch.cuda.synchronize()  # Wait for GPU if used (but we're on CPU)
end = time.time()
print(f"CPU time: {end - start:.4f} seconds")

# GPU test (if available)
if torch.cuda.is_available():
    a_gpu = a_cpu.cuda()
    b_gpu = b_cpu.cuda()
    
    # Warmup (GPU needs initial run)
    _ = a_gpu @ b_gpu
    torch.cuda.synchronize()
    
    start = time.time()
    result_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    end = time.time()
    print(f"GPU time: {end - start:.4f} seconds")
    
    # Verify results are close (they should be)
    diff = (result_cpu - result_gpu()).abs().max()
    print(f"Maximum difference between CPU and GPU results: {diff:.6f}")
    
    
'''
If you have a GPU, the GPU time is significantly faster (5-20x faster)
If no GPU, you'll only see the CPU time.
'''
