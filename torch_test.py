import torch

print("torch当前版本号:",torch.__version__) 
print("cuda版本号:",torch.version.cuda)  
if torch.cuda.is_available():
    print("GPU可用！")
else:
    print("GPU不可用，将使用CPU进行计算。")