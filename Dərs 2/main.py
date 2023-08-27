#cut ve tek oldugun yoxlayir

# İstifadəçidən ədəd daxil etməsini istəyirik
num = int(input("Ədəd daxil edin: "))

# Ədədin tək və ya cüt olduğunu yoxlayırıq
if num % 2 == 0:
    print("Daxil etdiyiniz ədəd cüt ədəddir.")
else:
    print("Daxil etdiyiniz ədəd tək ədəddir.")
