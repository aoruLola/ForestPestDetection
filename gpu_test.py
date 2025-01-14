import torch
flag = torch.cuda.is_available()
if flag:
    print("CUDA可使用")
else:
    print("CUDA不可用")

ngpu= 1
# Decide which device we want to run on
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print("驱动为：",device)
print("GPU型号： ",torch.cuda.get_device_name(0))


torch.cuda.is_available()
#cuda是否可用；

torch.cuda.device_count()
#返回gpu数量；

torch.cuda.get_device_name(0)
#返回gpu名字，设备索引默认从0开始；

torch.cuda.current_device()
#返回当前设备索引；
