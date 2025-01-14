
def show_menu():
    print("请选择一个选项：")
    print("1. 训练模型")
    print("2. 推理")
    print("3. 退出")

def train(): # 训练模型
    print("添加项功能")

def predict(): # 推理
    print("删除项功能")


def main():
     while True:
        show_menu()
        choice = input("请选择（1-3）：")
        
        if choice == '1':
            train()
        elif choice == '2':
            predict()
        elif choice == '3':
            print("退出程序...")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()
