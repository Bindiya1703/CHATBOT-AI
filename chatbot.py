print("------------------------------------------------------------------------------------------------------------------------------------------------------")
def simple_chatbot():

    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "hi":
            print("Bot: Hi there!")
        elif "how are you" in user_input:
            print("Bot: I'm just a bot, but I'm doing well! How can I assist you?")
        elif "can you please help me?" in user_input:
            print("Bot: yes! sure, how can i help you? ")
        elif "i want mobile " in user_input:
            print("Bot: yes sure!I give you further information.stay turned")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

def interested():
    
    user_input = []
    while True:
        user_input = input("You: ").lower()
        if user_input == "yes":
            print("Bot: which type of Mobile you want ?\nPlease select one of the two product lines given below to which your product belongs:\nType-1. key-pad Mobile\nType-2. Smart phone\nFor key-pad Mobile type 1, For Smart phone ,2...")
        elif user_input == "1":
            print("Bot:choose your interested company:\nType-1.Nokia\nType-2.Samsung\nType-3.Motorola")
        elif user_input == "nokia":
                print("Type of Nokia key-pad Mobiles:\nType-1 Nokia-105\nType-2 Nokia-106\nType-3 Nokia-216\nif you want more information about your interested Mobile then type of that Mobile model name!")
        elif "nokia-105" in user_input:
            print("Bot:Nokia-105 Details\nfeatures:32 MB RAM | 32 MB ROM , 4.5 cm (1.77 inch) Display , 5000 mAh Battery , Dual Sim \nprice:₹1,111")
        elif "nokia-106" in user_input:
            print("Bot:Nokia-106 Details\nfeatures:4 MB RAM | 4 MB ROM , 4.57 cm (1.8 inch) Display , 800 mAh Battery , Dual Sim \nprice:₹1,087")
        elif "nokia-216" in user_input:
            print("Bot:Nokia-216 Details\nfeatures:16 MB RAM | NA ROM | Expandable Upto 32 GB , 6.1 cm (2.4 inch) QVGA Display , 0.3MP Rear Camera | 0.3MP Front Camera , 1020 mAh Battery , Dual Sim \nprice:₹1,999")
        elif user_input == "samsung":
            print("Type of Samsung key-pad Mobiles:\nType-1 samsung-metro313\nType-2 samsung-gt1200\nType-3 samsung-gurumusic2\nType-4 samsung-guru fm plus\nif you want more information about your interested Mobile then type of that Mobile model name!")
        elif "samsung-metro313" in user_input:
            print("Bot:Samsung Metro 313 Details\nfeatures:4 MB RAM | 2.3 MB ROM | Expandable Upto 16 GB , 5.16 cm (2.03 inch) Display , 0.3MP Rear Camera , 1000 mAh Battery, Dual Sim \nprice:₹1,650")
        elif "samsung-gt1200" in user_input:
            print("Bot:Samsung GT 1200 Details\nfeatures:Model Name GT 1200 R/I/M ,Browse Type:Feature Phones, SIM Type:Single Sim \nprice:₹1,099")
        elif "samsung-gurumusic2" in user_input:
            print("Bot:samsung guru Music 2 Details\nfeatures:1 MB RAM | 32 MB ROM , 5.08 cm (2 inch) Display , 1MP Rear Camera , 800 mAh Battery\nprice:₹1,599")
        elif "samsung-guru fm plus" in user_input:
            print("Bot:Samsung Guru FM plus Details\nfeatures: SM-B110EABDINS , Model Name :Guru FM Plus SM-B110E/D , Browse Type:Feature Phones,Dual Sim\nprice:₹1,499")
        elif user_input == "motorola":
            print("Type of Motorola key-pad Mobiles:\nType-1 Motorola A10\nType-2 Motorola A10e\nType-3 Motorola A50 \nif you want more information about your interested Mobile then type of that Mobile model name!")
        elif user_input == "motorola a10":
            print("Bot:Motorola A10 Details\nfeatures: Motorola a10 Dual Sim keypad Mobile with 1750 mAh Battery, Expandable Storage Upto 32GB, Wireless FM with Recording\nprice:₹1,049")
        elif user_input == "motorola a10e":
            print("Bot:Motorola A10e Details\nfeatures: Motorola A10e Dual Sim keypad Mobile with 800 mAh Battery, Expandable Storage Upto 32GB, \nprice:₹999")
        elif user_input == "motorola a50":
            print("Bot:Motorola a50 Details\nfeatures: Motorola A50 - Dual Sim Keypad Phone with Long Lasting Battery, Expandable Memory Upto 32GB, Rear Camera, 1750 mAh Big Battery, 6 Indian Languages Input Support (Dark Blue)\nprice:₹1,999")
        elif user_input == "2":
            print("Bot:choose your interested company:\nType-1.Vivo\nType-2.Oppo\nType-3.Samsung\nType-4.Apple\nType-5.one plus\nType-6.Google\nType-7.Realme\nType-8.xiaomi")
        elif user_input == "vivo":
            print("Type of Vivo Smart Mobiles:\nType-1 Vivo-T2x\nType-2 Vivo-Y27\nType-3 Vivo-Y200\nif you want more information about your interested Mobile then type of that Mobile model name!")
        elif user_input == "vivo-t2x":
            print("Bot:Vivo-T2x Details\nfeatures: 6 GB RAM | 128 GB ROM ,16.71 cm (6.58 inch) Full HD+ Display , 50MP + 2MP | 8MP Front Camera , 5000 mAh Battery , Dimensity 6020 Processor\nprice:₹12,999")
        elif user_input == "vivo-y27":
            print("Bot:Vivo-T2x Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 8MP Selfie Camera with rear flash, night mode, Display: 16.86 cm (6.64 inch) FHD+ LCD Sunlight Display for enhanced outdoor display , Memory & SIM: 6 GB RAM | 128 GB \nprice:₹10,999")
        elif user_input == "vivo-y200":
            print("Bot:Vivo-Y200 Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹20,999")
        elif user_input == "apple":
            print("Type of Apple Smart Mobiles:\nType-1 I-phone 14\nType-2  I-phone 14 pro\nType-3  I-phone 14 pro max\nType-4  I-phone 15\nType-5  I-phone 15 pro\nType-6  I-phone 15 pro max\nif you want more information about your interested Mobile then type of that Mobile model name!")
        elif user_input == "i-phone 14":
            print("Bot:I-phone 14 Details\nfeatures:Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹65,000")
        elif user_input == "i-phone 14 pro":
            print("Bot:I-phone 14 pro Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹1,49,000")
        elif user_input == "i-phone 14 pro max":
            print("Bot:I-phone 14 pro max  Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹1,89,000")
        elif user_input == "i-phone 15":
            print("Bot:I-phone 15  Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹89,000")
        elif user_input == "i-phone 15 pro":
            print("Bot:I-phone 15 pro Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹1,49,000")
        elif user_input == "i-phone 15 pro max":
            print("Bot:I-phone 15 pro max Details\nfeatures: Camera: Dual 50MP+2MP Rear Camera | 16MP Selfie Camera Rear flash , Display: 16.94 cm 6.67 inch FHD+ AMOLED Capacitive multi-touch display 120Hz refresh rate, 394 ppi , Memory & SIM: 8GB RAM | 128GB internal memory; LPDDR4X | UFS 2.2\nprice:₹1,89,000")

        elif "i want to register" in user_input:
            print("Bot: yes sure!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

def register_user():
    user_data = {}
    print("Welcome to the registration process!")
    user_data['name'] = input("Please enter your name: ")
    user_data['address'] = input("Please enter your address: ")
    user_data['email'] = input("Please enter your email: ")
    user_data['mobile'] = input("Please enter your interested mobile: ")
    user_data['type of purchase'] = input("Please enter your type of purchase Type.1-monthly payment || Type.2 cash: ")
    print("Registration complete!")
    return user_data
registered_users = []

def main():
    while True:
        user_input = input("You: ").lower()
        if user_input == 'register':
            user_data = register_user()
            print(f"User {user_data['name']} registered successfull! Thank you for Registeration...")
        elif user_input == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'register' or 'exit'.")
if __name__ == "__main__":
    print("Bot: Hi! I'm a simple chatbot. How can I help you today?")
    simple_chatbot()
    print("Bot: Are you interested to getting Mobile information?")
    interested()
    print("Bot: Are you interested to register with us.Type 'register' to create a new account or 'exit' to quit: ")
    main()